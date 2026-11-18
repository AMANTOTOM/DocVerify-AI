import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from auth import create_token
from database import users

app = FastAPI()

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