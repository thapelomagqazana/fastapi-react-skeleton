"""
User API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.deps import get_current_user, get_db
from app.crud import user as user_crud
from app.schemas.user import UserCreate, UserOut, UserUpdate

router = APIRouter()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    existing_user = user_crud.get_user_by_email(db, user.email.lower())
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return user_crud.create_user(db, user)


@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get a list of all users.
    """
    return user_crud.get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserOut)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    """
    Get a specific user's details.
    """
    db_user = user_crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    updates: UserUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    """
    Update the current user's details.
    """
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to update this user.")
    
    db_user = user_crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    return user_crud.update_user(db, db_user, updates)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    """
    Delete the current user's account.
    """
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to delete this user.")

    db_user = user_crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    user_crud.delete_user(db, db_user)
