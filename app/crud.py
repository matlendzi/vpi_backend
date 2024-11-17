from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from app.models import VisitortypeData, AgeData, DwelltimeData

def get_visitor_types(db: Session, zone_id: str, date: date = None, VisitorType: str = None):
    """
    Retrieves aggregated visitor data by visitor types for a specific zone.

    Args:
        db (Session): SQLAlchemy database session.
        zone_id (str): Identifier for the zone to filter the data.
        date (date, optional): Specific date to filter the data. Defaults to None.
        VisitorType (str, optional): Specific visitor type to filter the data. Defaults to None.

    Returns:
        list[dict]: A list of dictionaries containing:
            - date (str): Date of the record.
            - VisitorType (str): Visitor type.
            - sum_num_visitors (float): Sum of visitors for the given type and zone.
    """
    # Build the base query
    query = db.query(
        VisitortypeData.date,
        VisitortypeData.VisitorType,
        func.sum(VisitortypeData.visitors).label("sum_num_visitors")
    ).filter(VisitortypeData.zone_id == zone_id)

    # Apply filters based on optional parameters
    if date:
        query = query.filter(VisitortypeData.date == date)
    if VisitorType:
        query = query.filter(VisitortypeData.VisitorType == VisitorType)

    # Group results and fetch data
    results = query.group_by(VisitortypeData.date, VisitortypeData.VisitorType).all()
    return [
        {"date": result.date, "VisitorType": result.VisitorType, "sum_num_visitors": result.sum_num_visitors}
        for result in results
    ]

def get_age_groups(db: Session, zone_id: str, date: date = None, age_group: str = None):
    """
    Retrieves aggregated visitor data by age groups for a specific zone.

    Args:
        db (Session): SQLAlchemy database session.
        zone_id (str): Identifier for the zone to filter the data.
        date (date, optional): Specific date to filter the data. Defaults to None.
        age_group (str, optional): Specific age group to filter the data. Defaults to None.

    Returns:
        list[dict]: A list of dictionaries containing:
            - date (str): Date of the record.
            - age_group (str): Age group of the visitors.
            - sum_num_visitors (float): Sum of visitors for the given age group and zone.
    """
    # Build the base query
    query = db.query(
        AgeData.date,
        AgeData.age_group,
        func.sum(AgeData.visitors).label("sum_num_visitors")
    ).filter(AgeData.zone_id == zone_id)

    # Apply filters based on optional parameters
    if date:
        query = query.filter(AgeData.date == date)
    if age_group:
        query = query.filter(AgeData.age_group == age_group)

    # Group results and fetch data
    results = query.group_by(AgeData.date, AgeData.age_group).all()
    return [
        {"date": result.date, "age_group": result.age_group, "sum_num_visitors": result.sum_num_visitors}
        for result in results
    ]

def get_dwell_times(db: Session, zone_id: str, date: date = None, DwellTime: str = None):
    """
    Retrieves aggregated visitor data by dwell times for a specific zone.

    Args:
        db (Session): SQLAlchemy database session.
        zone_id (str): Identifier for the zone to filter the data.
        date (date, optional): Specific date to filter the data. Defaults to None.
        DwellTime (str, optional): Specific dwell time to filter the data. Defaults to None.

    Returns:
        list[dict]: A list of dictionaries containing:
            - date (str): Date of the record.
            - DwellTime (str): Dwell time category.
            - sum_num_visitors (float): Sum of visitors for the given dwell time and zone.
    """
    # Build the base query
    query = db.query(
        DwelltimeData.date,
        DwelltimeData.DwellTime,
        func.sum(DwelltimeData.visitors).label("sum_num_visitors")
    ).filter(DwelltimeData.zone_id == zone_id)

    # Apply filters based on optional parameters
    if date:
        query = query.filter(DwelltimeData.date == date)
    if DwellTime:
        query = query.filter(DwelltimeData.DwellTime == DwellTime)

    # Group results and fetch data
    results = query.group_by(DwelltimeData.date, DwelltimeData.DwellTime).all()
    return [
        {"date": result.date, "DwellTime": result.DwellTime, "sum_num_visitors": result.sum_num_visitors}
        for result in results
    ]
