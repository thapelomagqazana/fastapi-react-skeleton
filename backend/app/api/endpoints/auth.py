"""
Auth endpoints for login.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..deps import get_db
from ...crud.user import get_user_by_email
from ...core.security import verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter()

class AuthDetails(BaseModel):
    """Schema for login."""
    email: str
    password: str

@router.post("/signin")
def signin(auth_details: AuthDetails, db: Session = Depends(get_db)):
    """
    Authenticate a user and return JWT token.
    """
    user = get_user_by_email(db, auth_details.email)
    if not user or not verify_password(auth_details.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}
