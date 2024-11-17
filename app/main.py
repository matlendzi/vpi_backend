from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from datetime import date

# Initialize the FastAPI application
app = FastAPI()

# Visitor Types Endpoint
@app.get("/visitor-types/")
def get_visitor_types(
    zone_id: str,                               # Required query parameter for zone identifier
    group_by_date: date = Query(None, alias="group_by[date]"),  # Optional filter for date
    VisitorType: str = Query(None, alias="VisitorType"),        # Optional filter for visitor type
    db: Session = Depends(get_db)              # Database session injected using dependency
):
    """
    Endpoint to retrieve aggregated visitor data by visitor types.

    Args:
        zone_id (str): Identifier for the zone.
        group_by_date (date, optional): Date to filter the results. Defaults to None.
        VisitorType (str, optional): Specific visitor type to filter the data. Defaults to None.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        dict: A JSON response containing the aggregated data.

    Raises:
        HTTPException: 404 error if no data is found for the given parameters.
    """
    visitor_data = crud.get_visitor_types(db, zone_id=zone_id, date=group_by_date, VisitorType=VisitorType)
    if not visitor_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")
    return {"data": visitor_data}

# Ages Endpoint
@app.get("/ages/")
def get_age_groups(
    zone_id: str,                               # Required query parameter for zone identifier
    group_by_date: date = Query(None, alias="group_by[date]"),  # Optional filter for date
    age_group: str = Query(None, alias="age_group"),            # Optional filter for age group
    db: Session = Depends(get_db)              # Database session injected using dependency
):
    """
    Endpoint to retrieve aggregated visitor data by age groups.

    Args:
        zone_id (str): Identifier for the zone.
        group_by_date (date, optional): Date to filter the results. Defaults to None.
        age_group (str, optional): Specific age group to filter the data. Defaults to None.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        dict: A JSON response containing the aggregated data.

    Raises:
        HTTPException: 404 error if no data is found for the given parameters.
    """
    age_data = crud.get_age_groups(db, zone_id=zone_id, date=group_by_date, age_group=age_group)
    if not age_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")
    return {"data": age_data}

# Dwell Times Endpoint
@app.get("/dwell-times/")
def get_dwell_times(
    zone_id: str,                               # Required query parameter for zone identifier
    group_by_date: date = Query(None, alias="group_by[date]"),  # Optional filter for date
    DwellTime: str = Query(None, alias="DwellTime"),            # Optional filter for dwell time category
    db: Session = Depends(get_db)              # Database session injected using dependency
):
    """
    Endpoint to retrieve aggregated visitor data by dwell times.

    Args:
        zone_id (str): Identifier for the zone.
        group_by_date (date, optional): Date to filter the results. Defaults to None.
        DwellTime (str, optional): Specific dwell time category to filter the data. Defaults to None.
        db (Session): SQLAlchemy database session (injected).

    Returns:
        dict: A JSON response containing the aggregated data.

    Raises:
        HTTPException: 404 error if no data is found for the given parameters.
    """
    dwell_data = crud.get_dwell_times(db, zone_id=zone_id, date=group_by_date, DwellTime=DwellTime)
    if not dwell_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")
    return {"data": dwell_data}
