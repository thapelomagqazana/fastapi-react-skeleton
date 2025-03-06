from .db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Extract the user ID from the JWT token.
    """
    try:
        payload = verify_access_token(token)
        return payload.get("user_id")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

def get_db() -> Generator:
    """
    Dependency to get a DB session.
    Closes the session after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
