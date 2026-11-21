from datetime import UTC, datetime
from typing import Annotated, Literal

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from auth import require_role
from database import applications, documents

router = APIRouter(prefix="/review")

Reviewer = Annotated[dict, Depends(require_role("reviewer", "admin"))]


class DocumentReview(BaseModel):
    status: Literal["Approved", "Rejected"]
    comment: str = ""


class ApplicationStatus(BaseModel):
    status: Literal["In review", "Approved", "Rejected"]


def to_object_id(value: str) -> ObjectId:
    try:
        return ObjectId(value)
    except InvalidId:
        raise HTTPException(status_code=404, detail="Not found") from None


def document_view(d: dict) -> dict:
    return {
        "id": str(d["_id"]),
        "document_type": d["document_type"],
        "filename": d["original_name"],
        "notes": d["notes"],
        "status": d["status"],
        "review_comment": d.get("review_comment", ""),
    }


@router.get("/applications")
def list_all_applications(user: Reviewer, status: str | None = None):
    query = {"status": status} if status else {}
    result = []
    for application in applications.find(query):
        count = documents.count_documents({"application_id": str(application["_id"])})
        result.append(
            {
                "id": str(application["_id"]),
                "owner": application["owner"],
                "status": application["status"],
                "document_count": count,
            }
        )
    return result


@router.get("/applications/{application_id}")
def get_application(application_id: str, user: Reviewer):
    application = applications.find_one({"_id": to_object_id(application_id)})
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    docs = documents.find({"application_id": application_id})
    return {
        "id": application_id,
        "owner": application["owner"],
        "status": application["status"],
        "documents": [document_view(d) for d in docs],
    }


@router.patch("/documents/{document_id}")
def review_document(document_id: str, review: DocumentReview, user: Reviewer):
    result = documents.update_one(
        {"_id": to_object_id(document_id)},
        {
            "$set": {
                "status": review.status,
                "review_comment": review.comment,
                "reviewed_by": user["email"],
                "reviewed_at": datetime.now(UTC),
            }
        },
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"id": document_id, "status": review.status}


@router.patch("/applications/{application_id}")
def set_application_status(application_id: str, body: ApplicationStatus, user: Reviewer):
    result = applications.update_one(
        {"_id": to_object_id(application_id)}, {"$set": {"status": body.status}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"id": application_id, "status": body.status}