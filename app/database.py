import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(level=logging.INFO)

# Environment variable for the database URL, defaulting to SQLite with `database.db`
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/database.db")

# Create the SQLAlchemy engine
try:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    logging.info("Database connection established successfully.")
except Exception as e:
    logging.error(f"Failed to connect to the database: {e}")
    raise

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()

def get_db():
    """
    Dependency function to provide a database session.

    Yields:
        db (SessionLocal): A new database session.
    Closes:
        The session after use to free resources.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
