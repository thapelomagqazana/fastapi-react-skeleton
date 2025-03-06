from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.crud import user as user_crud
from app.utils.security import verify_password
from app.utils.jwt import create_access_token
from app.schemas.auth import SignInRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signin", response_model=TokenResponse)
def signin(credentials: SignInRequest, db: Session = Depends(get_db)):
    """
    Authenticate a user and return a JWT token.
    """
    db_user = user_crud.get_user_by_email(db, credentials.email)
    if not db_user or not verify_password(credentials.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token({"user_id": db_user.id})
    return {"access_token": access_token}


@router.post("/signout")
def signout():
    """
    (Optional) Sign out user (for stateless JWT, this is just a client-side token delete).
    """
    return {"message": "Sign-out successful (token deleted client-side)"}
