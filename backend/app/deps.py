from .db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

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
