"""
User API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from sqlalchemy.orm import Session
from typing import List

from app.deps import get_current_user, get_db
from app.crud import user as user_crud
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.db.models import User

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
def read_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=10000), 
    db: Session = Depends(get_db)
):
    """
    Get a list of all users.
    """
    return user_crud.get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserOut)
def read_user(
    user_id: int = Path(..., gt=0),
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
    current_user: User = Depends(get_current_user)
):
    """
    Update the current user's details or allow admin to update any user.
    """    
    db_user = user_crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    if user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized to update this user.")

    return user_crud.update_user(db, db_user, updates)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete the current user's account or allow admin to delete any user.
    """
    db_user = user_crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    if user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized to delete this user.")

    user_crud.delete_user(db, db_user)
