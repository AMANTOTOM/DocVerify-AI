import uuid

import pytest
from fastapi.testclient import TestClient
from pymongo.errors import PyMongoError

from database import applications, documents, users
from database import client as mongo
from main import app

client = TestClient(app)
PASSWORD = "password123"


@pytest.fixture(scope="module", autouse=True)
def need_mongo():
    try:
        mongo.admin.command("ping")
    except PyMongoError:
        pytest.skip("MongoDB is not running")

def make_user(role):
    email = f"{uuid.uuid4().hex[:8]}@example.com"
    client.post("/register", json={"email": email, "password": PASSWORD})
    users.update_one({"email": email}, {"$set": {"role": role}})
    response = client.post("/login", json={"email": email, "password": PASSWORD})
    headers = {"Authorization": f"Bearer {response.json()['access_token']}"}
    return email, headers


def upload(headers, application_id, filename="cv.pdf", content_type="application/pdf"):
    return client.post(
        f"/applications/{application_id}/documents",
        headers=headers,
        data={"document_type": "cv", "notes": "test"},
        files=[("files", (filename, b"%PDF-1.4 test", content_type))],
    )


def test_applicant_uploads_and_reviewer_approves():
    applicant_email, applicant = make_user("applicant")
    reviewer_email, reviewer = make_user("reviewer")
    try:
        application_id = client.post("/applications", headers=applicant).json()["id"]

        uploaded = upload(applicant, application_id)
        assert uploaded.status_code == 201
        document_id = uploaded.json()[0]["id"]

        mine = client.get("/applications", headers=applicant).json()
        assert mine[0]["documents"][0]["status"] == "Submitted"

        review = client.patch(
            f"/review/documents/{document_id}",
            headers=reviewer,
            json={"status": "Approved", "comment": "ok"},
        )
        assert review.status_code == 200

        detail = client.get(f"/review/applications/{application_id}", headers=reviewer)
        assert detail.json()["documents"][0]["status"] == "Approved"
    finally:
        for email in (applicant_email, reviewer_email):
            users.delete_one({"email": email})
        applications.delete_many({"owner": applicant_email})
        documents.delete_many({"owner": applicant_email})


def test_wrong_file_type_is_refused():
    email, applicant = make_user("applicant")
    try:
        application_id = client.post("/applications", headers=applicant).json()["id"]
        response = upload(applicant, application_id, "notes.txt", "text/plain")
        assert response.status_code == 400
    finally:
        users.delete_one({"email": email})
        applications.delete_many({"owner": email})


def test_applicant_cannot_use_review_routes():
    email, applicant = make_user("applicant")
    try:
        response = client.get("/review/applications", headers=applicant)
        assert response.status_code == 403
    finally:
        users.delete_one({"email": email})

def test_admin_changes_role_but_not_own():
    admin_email, admin = make_user("admin")
    user_email, _ = make_user("applicant")
    try:
        own = client.patch(
            f"/admin/users/{admin_email}/role", headers=admin, json={"role": "reviewer"}
        )
        assert own.status_code == 400

        changed = client.patch(
            f"/admin/users/{user_email}/role", headers=admin, json={"role": "reviewer"}
        )
        assert changed.status_code == 200
        assert users.find_one({"email": user_email})["role"] == "reviewer"
    finally:
        for email in (admin_email, user_email):
            users.delete_one({"email": email})