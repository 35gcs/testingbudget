from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import os
import secrets

# CRITICAL: SECRET_KEY must be set in production
# Generate a secure random key with: python -c "import secrets; print(secrets.token_urlsafe(32))"
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    import logging
    # Generate a random key for development, but warn loudly
    SECRET_KEY = secrets.token_urlsafe(32)
    logging.warning(
        "⚠️  WARNING: SECRET_KEY not set! Using random key. "
        "Set SECRET_KEY environment variable in production!"
    )

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60  # 30 days

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        return user_id
    except JWTError:
        return None
