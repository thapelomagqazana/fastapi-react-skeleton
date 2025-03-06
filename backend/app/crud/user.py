"""
CRUD operations for User model.
"""

from sqlalchemy.orm import Session
from ..db import models, schemas
from ..core.security import hash_password

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """Create a new user."""
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> models.User:
    """Retrieve a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session) -> list[models.User]:
    """Retrieve all users."""
    return db.query(models.User).all()

def get_user(db: Session, user_id: int) -> models.User:
    """Retrieve a user by ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()
