from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import VisitortypeData, AgeData, DwelltimeData, DailyFrequencyData

def get_hourly_aggregated(db: Session, zone_id: str, date__gte=None, date__lte=None):
    """
    Fetch hourly aggregated visitor data for a zone and date range.

    Args:
        db (Session): SQLAlchemy database session.
        zone_id (str): Identifier for the zone.
        date__gte (str, optional): Start of the date range.
        date__lte (str, optional): End of the date range.

    Returns:
        list[dict]: Hourly aggregated data.
    """
    query = db.query(
        func.strftime("%H", DailyFrequencyData.date).label("date_hour"),  # Extract hour from datetime
        func.sum(DailyFrequencyData.Count).label("sum_num_visitors")
    ).filter(
        DailyFrequencyData.zone_id == zone_id  # Filter by zone_id
    )

    # Apply date range filters if provided
    if date__gte:
        query = query.filter(DailyFrequencyData.date >= date__gte)
    if date__lte:
        query = query.filter(DailyFrequencyData.date <= date__lte)

    query = query.group_by(
        func.strftime("%H", DailyFrequencyData.date)  # Group by hour
    ).order_by(
        func.strftime("%H", DailyFrequencyData.date)  # Sort by hour
    )

    results = query.all()
    return [
        {"date__hour": int(result.date_hour), "sum_num_visitors": float(result.sum_num_visitors)}
        for result in results
    ]

def get_daily_aggregated(db: Session, zone_id: str, date=None, date__gte=None, date__lte=None):
    """
    Fetch daily aggregated visitor data for a zone and date range.

    Args:
        db (Session): SQLAlchemy database session.
        zone_id (str): Identifier for the zone.
        date (str, optional): Specific date.
        date__gte (str, optional): Start of the date range.
        date__lte (str, optional): End of the date range.

    Returns:
        list[dict]: Daily aggregated data.
    """
    query = db.query(
        func.date(DailyFrequencyData.date).label("date"),
        func.sum(DailyFrequencyData.Count).label("sum_num_visitors")
    ).filter(
        DailyFrequencyData.zone_id == zone_id
    )

    if date:
        query = query.filter(func.date(DailyFrequencyData.date) == date)
    if date__gte:
        query = query.filter(DailyFrequencyData.date >= date__gte)
    if date__lte:
        query = query.filter(DailyFrequencyData.date <= date__lte)

    query = query.group_by(
        func.date(DailyFrequencyData.date)
    ).order_by(
        func.date(DailyFrequencyData.date)
    )

    results = query.all()
    return [
        {"date": str(result.date), "sum_num_visitors": float(result.sum_num_visitors)}
        for result in results
    ]

def get_visitor_types(db: Session, zone_id: str, date=None, VisitorType=None):
    query = db.query(
        VisitortypeData.date,
        VisitortypeData.VisitorType,
        func.sum(VisitortypeData.visitors).label("sum_num_visitors")
    ).filter(VisitortypeData.zone_id == zone_id)

    if date:
        query = query.filter(func.date(VisitortypeData.date) == date)
    if VisitorType:
        query = query.filter(VisitortypeData.VisitorType == VisitorType)

    query = query.group_by(VisitortypeData.date, VisitortypeData.VisitorType).order_by(VisitortypeData.date)

    results = query.all()

    return [
        {"date": str(result.date), "VisitorType": result.VisitorType, "sum_num_visitors": float(result.sum_num_visitors)}
        for result in results
    ]

def get_age_groups(db: Session, zone_id: str, date=None, age_group=None):
    query = db.query(
        AgeData.date,
        AgeData.age_group,
        func.sum(AgeData.visitors).label("sum_num_visitors")
    ).filter(AgeData.zone_id == zone_id)

    if date:
        query = query.filter(func.date(AgeData.date) == date)
    if age_group:
        query = query.filter(AgeData.age_group == age_group)

    query = query.group_by(AgeData.date, AgeData.age_group).order_by(AgeData.date)

    results = query.all()

    return [
        {"date": str(result.date), "age_group": result.age_group, "sum_num_visitors": float(result.sum_num_visitors)}
        for result in results
    ]

def get_dwell_times(db: Session, zone_id: str, date=None, DwellTime=None):
    query = db.query(
        DwelltimeData.date,
        DwelltimeData.DwellTime,
        func.sum(DwelltimeData.visitors).label("sum_num_visitors")
    ).filter(DwelltimeData.zone_id == zone_id)

    if date:
        query = query.filter(func.date(DwelltimeData.date) == date)
    if DwellTime:
        query = query.filter(DwelltimeData.DwellTime == DwellTime)

    query = query.group_by(DwelltimeData.date, DwelltimeData.DwellTime).order_by(DwelltimeData.date)

    results = query.all()

    return [
        {"date": str(result.date), "DwellTime": result.DwellTime, "sum_num_visitors": float(result.sum_num_visitors)}
        for result in results
    ]
