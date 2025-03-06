"""
CRUD operations for the User model.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import models
from app.schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """
    Hashes a plain-text password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that a plain-text password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_user(db: Session, user: UserCreate) -> models.User:
    """
    Create a new user in the database.
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Retrieve a user by their ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    Retrieve a user by their email.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    """
    Retrieve all users with pagination.
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, db_user: models.User, updates: UserUpdate) -> models.User:
    """
    Update an existing user's details.
    """
    if updates.name:
        db_user.name = updates.name
    if updates.email:
        db_user.email = updates.email
    if updates.password:
        db_user.hashed_password = get_password_hash(updates.password)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: models.User) -> None:
    """
    Delete a user from the database.
    """
    db.delete(db_user)
    db.commit()
