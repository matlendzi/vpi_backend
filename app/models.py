from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from app.database import Base

class VisitortypeData(Base):
    """
    SQLAlchemy model for the `visitortype_data` table.
    """
    __tablename__ = "visitortype_data"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(DateTime, index=True)
    zone_id = Column(String, index=True)
    VisitorType = Column(String)

    # Composite index for efficient filtering
    __table_args__ = (Index("idx_zone_id_date", "zone_id", "date"),)


class AgeData(Base):
    """
    SQLAlchemy model for the `age_data` table.
    """
    __tablename__ = "age_data"
    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(String, index=True)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(DateTime, index=True)
    age_group = Column(String)

    # Composite index for efficient filtering
    __table_args__ = (Index("idx_zone_id_date", "zone_id", "date"),)


class DwelltimeData(Base):
    """
    SQLAlchemy model for the `dwelltime_data` table.
    """
    __tablename__ = "dwelltime_data"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(DateTime, index=True)
    zone_id = Column(String, index=True)
    DwellTime = Column(String)

    # Composite index for efficient filtering
    __table_args__ = (Index("idx_zone_id_date", "zone_id", "date"),)


class DailyFrequencyData(Base):
    """
    SQLAlchemy model for the `dailyfrequency_data` table.
    """
    __tablename__ = "dailyfrequency_data"
    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(String, index=True)
    date = Column(DateTime, index=True)
    Count = Column(Float)
    ReiseArt = Column(String)
    ReiseDistanz = Column(String)

    # Composite index for efficient filtering
    __table_args__ = (Index("idx_zone_id_date", "zone_id", "date"),)
