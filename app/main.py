from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from datetime import date

app = FastAPI()

# Visitor Types Endpoint
@app.get("/visitor-types/")
def get_visitor_types(
    zone_id: str,
    group_by_date: date = Query(None, alias="group_by[date]"),
    VisitorType: str = Query(None, alias="VisitorType"),
    db: Session = Depends(get_db)
):
    visitor_data = crud.get_visitor_types(db, zone_id=zone_id, date=group_by_date, VisitorType=VisitorType)
    if not visitor_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")

    return {"data": visitor_data}

# Ages Endpoint
@app.get("/ages/")
def get_age_groups(
    zone_id: str,
    group_by_date: date = Query(None, alias="group_by[date]"),
    age_group: str = Query(None, alias="age_group"),
    db: Session = Depends(get_db)
):
    age_data = crud.get_age_groups(db, zone_id=zone_id, date=group_by_date, age_group=age_group)
    if not age_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")

    return {"data": age_data}

# Dwell Times Endpoint
@app.get("/dwell-times/")
def get_dwell_times(
    zone_id: str,
    group_by_date: date = Query(None, alias="group_by[date]"),
    DwellTime: str = Query(None, alias="DwellTime"),
    db: Session = Depends(get_db)
):
    dwell_data = crud.get_dwell_times(db, zone_id=zone_id, date=group_by_date, DwellTime=DwellTime)
    if not dwell_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")

    return {"data": dwell_data}

