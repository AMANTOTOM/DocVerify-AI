import os
from datetime import UTC, datetime, timedelta

import jwt

ALGORITHM = "HS256"


def create_token(email: str, role: str) -> str:
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("SECRET_KEY is not set")
    expires = datetime.now(UTC) + timedelta(hours=8)
    payload = {"sub": email, "role": role, "exp": expires}
    return jwt.encode(payload, secret_key, algorithm=ALGORITHM)