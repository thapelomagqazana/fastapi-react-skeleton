"""
Pydantic schemas for request and response validation.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """
    Schema for creating a user.
    """
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    """
    Schema for returning user data.
    """
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    """
    Schema for updating user data.
    """
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
