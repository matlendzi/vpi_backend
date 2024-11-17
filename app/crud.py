from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from app.models import VisitortypeData, AgeData, DwelltimeData

def get_visitor_types(db: Session, zone_id: str, date: date = None, VisitorType: str = None):
    query = db.query(
        VisitortypeData.date,
        VisitortypeData.VisitorType,
        func.sum(VisitortypeData.visitors).label("sum_num_visitors")
    ).filter(VisitortypeData.zone_id == zone_id)

    if date:
        query = query.filter(VisitortypeData.date == date)
    if VisitorType:
        query = query.filter(VisitortypeData.VisitorType == VisitorType)

    results = query.group_by(VisitortypeData.date, VisitortypeData.VisitorType).all()
    return [{"date": result.date, "VisitorType": result.VisitorType, "sum_num_visitors": result.sum_num_visitors} for result in results]

def get_age_groups(db: Session, zone_id: str, date: date = None, age_group: str = None):
    query = db.query(
        AgeData.date,
        AgeData.age_group,
        func.sum(AgeData.visitors).label("sum_num_visitors")
    ).filter(AgeData.zone_id == zone_id)

    if date:
        query = query.filter(AgeData.date == date)
    if age_group:
        query = query.filter(AgeData.age_group == age_group)

    results = query.group_by(AgeData.date, AgeData.age_group).all()
    return [{"date": result.date, "age_group": result.age_group, "sum_num_visitors": result.sum_num_visitors} for result in results]

def get_dwell_times(db: Session, zone_id: str, date: date = None, DwellTime: str = None):
    query = db.query(
        DwelltimeData.date,
        DwelltimeData.DwellTime,
        func.sum(DwelltimeData.visitors).label("sum_num_visitors")
    ).filter(DwelltimeData.zone_id == zone_id)

    if date:
        query = query.filter(DwelltimeData.date == date)
    if DwellTime:
        query = query.filter(DwelltimeData.DwellTime == DwellTime)

    results = query.group_by(DwelltimeData.date, DwelltimeData.DwellTime).all()
    return [{"date": result.date, "DwellTime": result.DwellTime, "sum_num_visitors": result.sum_num_visitors} for result in results]

