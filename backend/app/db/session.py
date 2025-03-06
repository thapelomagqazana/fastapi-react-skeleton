"""
Database connection handler using SQLAlchemy and PostgreSQL.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Validate that DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Optional: Logs all SQL statements (remove in production)
)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(
    autocommit=False,  # We manage transactions manually
    autoflush=False,  # Disable automatic flush
    bind=engine       # Connect the session to the engine
)
