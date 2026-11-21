from typing import Annotated

import bcrypt
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from auth import create_token, get_current_user, require_role
from database import users
from documents import router as documents_router
from reviewer import router as reviewer_router

app = FastAPI()
app.include_router(documents_router)
app.include_router(reviewer_router)

@app.get("/")
def home():
    return {"message": "backend is running"}
class RegisterRequest(BaseModel):
    email: str
    password: str


@app.post("/register", status_code=201)
def register(data: RegisterRequest):
    email = data.email.strip().lower()
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Please enter a valid email address")
    if len(data.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")
    if users.find_one({"email": email}):
        raise HTTPException(status_code=409, detail="This email is already registered")

    password_hash = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt())
    users.insert_one({"email": email, "password_hash": password_hash, "role": "applicant"})
    return {"message": "Account created"}

class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(data: LoginRequest):
    email = data.email.strip().lower()
    user = users.find_one({"email": email})
    if user is None or not bcrypt.checkpw(data.password.encode("utf-8"), user["password_hash"]):
        raise HTTPException(status_code=401, detail="Wrong email or password")

    token = create_token(email, user["role"])
    return {"access_token": token, "token_type": "bearer", "role": user["role"]}

CurrentUser = Annotated[dict, Depends(get_current_user)]
AdminUser = Annotated[dict, Depends(require_role("admin"))]


@app.get("/me")
def me(user: CurrentUser):
    return user


@app.get("/admin/users")
def list_users(user: AdminUser):
    return [{"email": u["email"], "role": u["role"]} for u in users.find()]