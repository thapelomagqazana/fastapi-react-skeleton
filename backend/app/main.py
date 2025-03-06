"""
FastAPI application entry point.
"""

from fastapi import FastAPI
from .api.endpoints import users, auth
from .db.models import Base
from .db.session import engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
