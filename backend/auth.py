import os
from datetime import UTC, datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

ALGORITHM = "HS256"


def create_token(email: str, role: str) -> str:
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("SECRET_KEY is not set")
    expires = datetime.now(UTC) + timedelta(hours=8)
    payload = {"sub": email, "role": role, "exp": expires}
    return jwt.encode(payload, secret_key, algorithm=ALGORITHM)

bearer_scheme = HTTPBearer()


def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)]):
    secret_key = os.getenv("SECRET_KEY")
    try:
        payload = jwt.decode(credentials.credentials, secret_key, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"email": payload["sub"], "role": payload["role"]}


def require_role(*allowed_roles):
    def checker(user: Annotated[dict, Depends(get_current_user)]):
        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="You do not have access to this")
        return user

    return checker