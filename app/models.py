from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class VisitortypeData(Base):
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
    __tablename__ = "dwelltime_data"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String)
    weekday = Column(String)
    quarter = Column(String)
    visitors = Column(Float)
    date = Column(String)
    zone_id = Column(String)
    DwellTime = Column(String)

