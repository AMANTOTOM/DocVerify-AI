import pytest
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.testclient import TestClient

from auth import create_token, get_current_user
from main import app

client = TestClient(app)


def test_token_round_trip():
    token = create_token("anna@example.com", "applicant")
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)
    assert get_current_user(credentials) == {"email": "anna@example.com", "role": "applicant"}


def test_token_needs_secret_key(monkeypatch):
    monkeypatch.delenv("SECRET_KEY", raising=False)
    with pytest.raises(RuntimeError):
        create_token("anna@example.com", "applicant")


def test_me_without_token_is_refused():
    assert client.get("/me").status_code in (401, 403)


def test_review_routes_without_token_are_refused():
    assert client.get("/review/applications").status_code in (401, 403)


def test_admin_routes_without_token_are_refused():
    assert client.get("/admin/users").status_code in (401, 403)