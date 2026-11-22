from typing import Annotated, Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from auth import require_role
from database import users

router = APIRouter(prefix="/admin")

Admin = Annotated[dict, Depends(require_role("admin"))]


class RoleChange(BaseModel):
    role: Literal["applicant", "reviewer", "admin"]


@router.patch("/users/{email}/role")
def change_role(email: str, change: RoleChange, user: Admin):
    if email == user["email"]:
        raise HTTPException(status_code=400, detail="You cannot change your own role")
    result = users.update_one({"email": email}, {"$set": {"role": change.role}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": email, "role": change.role}


@router.delete("/users/{email}")
def delete_user(email: str, user: Admin):
    if email == user["email"]:
        raise HTTPException(status_code=400, detail="You cannot delete yourself")
    result = users.delete_one({"email": email})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": email}