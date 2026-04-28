import hashlib
import secrets
from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.settings import settings


ALGORITHM = "HS256"


def create_access_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=3)
    }

    return jwt.encode(payload, settings.JWT_SECRET_KEY, ALGORITHM)

def create_refresh_token() -> tuple[str, str]:
    raw = secrets.token_urlsafe(32)
    hashed = hashlib.sha256(raw.encode()).hexdigest()
    return raw, hashed
