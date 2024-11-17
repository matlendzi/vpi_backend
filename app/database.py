from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL for the SQLite database connection
# Update the URL as needed to switch to a different database (e.g., PostgreSQL or MySQL)
DATABASE_URL = "sqlite:///./poc_data.db"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False} is specific to SQLite and allows multiple threads to access the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
# autocommit=False: Transactions need to be explicitly committed
# autoflush=False: Changes to the objects are not automatically flushed to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
# Models will inherit from this base class to define database tables
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
        yield db  # Provide the session to the caller
    finally:
        db.close()  # Close the session after use to release database connections
