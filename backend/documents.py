import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from auth import require_role
from database import applications, documents

router = APIRouter()

UPLOAD_DIR = Path("uploads")
MAX_SIZE = 10 * 1024 * 1024
ALLOWED_TYPES = {"application/pdf": ".pdf", "image/jpeg": ".jpg", "image/png": ".png"}
DOCUMENT_TYPES = [
    "degree certificate",
    "transcript",
    "language certificate",
    "passport",
    "cv",
    "other",
]

Applicant = Annotated[dict, Depends(require_role("applicant"))]


def get_own_application(application_id: str, user: dict):
    try:
        object_id = ObjectId(application_id)
    except InvalidId:
        raise HTTPException(status_code=404, detail="Application not found")
    application = applications.find_one({"_id": object_id, "owner": user["email"]})
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return application


@router.post("/applications", status_code=201)
def create_application(user: Applicant):
    result = applications.insert_one(
        {"owner": user["email"], "status": "Submitted", "created_at": datetime.now(UTC)}
    )
    return {"id": str(result.inserted_id), "status": "Submitted"}


@router.post("/applications/{application_id}/documents", status_code=201)
async def upload_documents(
    application_id: str,
    user: Applicant,
    document_type: Annotated[str, Form()],
    files: Annotated[list[UploadFile], File()],
    notes: Annotated[str, Form()] = "",
):
    application = get_own_application(application_id, user)
    if document_type not in DOCUMENT_TYPES:
        raise HTTPException(status_code=400, detail="Unknown document type")

    checked = []
    for file in files:
        extension = ALLOWED_TYPES.get(file.content_type)
        if extension is None:
            raise HTTPException(status_code=400, detail="Only PDF, JPG and PNG files are allowed")
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="The file is empty")
        if len(content) > MAX_SIZE:
            raise HTTPException(status_code=400, detail="The file is larger than 10 MB")
        checked.append((file.filename, file.content_type, extension, content))

    UPLOAD_DIR.mkdir(exist_ok=True)
    saved = []
    for filename, content_type, extension, content in checked:
        stored_name = f"{uuid.uuid4()}{extension}"
        (UPLOAD_DIR / stored_name).write_bytes(content)
        result = documents.insert_one(
            {
                "application_id": str(application["_id"]),
                "owner": user["email"],
                "document_type": document_type,
                "notes": notes,
                "original_name": filename,
                "stored_name": stored_name,
                "content_type": content_type,
                "size": len(content),
                "status": "Submitted",
                "uploaded_at": datetime.now(UTC),
            }
        )
        saved.append({"id": str(result.inserted_id), "filename": filename, "status": "Submitted"})
    return saved


@router.get("/applications")
def list_applications(user: Applicant):
    result = []
    for application in applications.find({"owner": user["email"]}):
        docs = documents.find({"application_id": str(application["_id"])})
        result.append(
            {
                "id": str(application["_id"]),
                "status": application["status"],
                "documents": [
                    {
                        "id": str(d["_id"]),
                        "document_type": d["document_type"],
                        "filename": d["original_name"],
                        "status": d["status"],
                    }
                    for d in docs
                ],
            }
        )
    return result