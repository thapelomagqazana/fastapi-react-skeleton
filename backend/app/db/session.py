"""
Database session and engine setup using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal is a factory to create new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
