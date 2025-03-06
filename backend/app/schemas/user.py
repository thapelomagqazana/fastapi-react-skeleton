"""
Pydantic schemas for User model.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Schema for creating a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# Schema for returning user data (output)
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        model_config = {
            "from_attributes": True
        } # Tells Pydantic to convert ORM objects to JSON


# Schema for updating an existing user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
