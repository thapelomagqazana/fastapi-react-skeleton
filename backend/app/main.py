from fastapi import FastAPI
from .api.endpoints import auth, users
from .db.models import Base
from .db.session import engine

# Create tables (optional during development)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
