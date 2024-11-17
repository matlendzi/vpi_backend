from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class VisitortypeData(Base):
    """
    SQLAlchemy model for the `visitortype_data` table.
    This table stores data about visitor types for specific zones.

    Attributes:
        id (int): Primary key, unique identifier for each record.
        hour (str): Hour of data collection.
        weekday (str): Weekday of data collection.
        quarter (str): Quarter of the year (e.g., Q1, Q2).
        visitors (float): Number of visitors.
        date (str): Date of the record.
        zone_id (str): Identifier for the zone.
        VisitorType (str): Type of visitor (e.g., tourist, local).
    """
    __tablename__ = "visitortype_data"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(String)
    zone_id = Column(String)
    VisitorType = Column(String)

class AgeData(Base):
    """
    SQLAlchemy model for the `age_data` table.
    This table stores data about the age groups of visitors for specific zones.

    Attributes:
        id (int): Primary key, unique identifier for each record.
        zone_id (str): Identifier for the zone.
        hour (str): Hour of data collection.
        weekday (str): Weekday of data collection.
        quarter (str): Quarter of the year (e.g., Q1, Q2).
        visitors (float): Number of visitors.
        date (str): Date of the record.
        age_group (str): Age group of the visitors (e.g., 18-25, 26-35).
    """
    __tablename__ = "age_data"
    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(String)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(String)
    age_group = Column(String)

class DwelltimeData(Base):
    """
    SQLAlchemy model for the `dwelltime_data` table.
    This table stores data about the dwell times of visitors in specific zones.

    Attributes:
        id (int): Primary key, unique identifier for each record.
        hour (str): Hour of data collection.
        weekday (str): Weekday of data collection.
        quarter (str): Quarter of the year (e.g., Q1, Q2).
        visitors (float): Number of visitors.
        date (str): Date of the record.
        zone_id (str): Identifier for the zone.
        DwellTime (str): Dwell time category (e.g., 0-5 min, 6-15 min).
    """
    __tablename__ = "dwelltime_data"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(String)
    zone_id = Column(String)
    DwellTime = Column(String)
