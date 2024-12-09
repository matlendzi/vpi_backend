from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from datetime import date
import os

# Initialize the FastAPI application
app = FastAPI()

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Global Middleware for JSON Content-Type
@app.middleware("http")
async def add_json_header(request, call_next):
    response = await call_next(request)
    response.headers["Content-Type"] = "application/json"
    return response

# Visitor Types Endpoint
@app.get("/visitor-types/")
def get_visitor_types(
    zone_id: str,
    date: date = Query(None),  # Accept date in YYYY-MM-DD format
    VisitorType: str = Query(None, alias="VisitorType"),
    db: Session = Depends(get_db)
):
    visitor_data = crud.get_visitor_types(db, zone_id=zone_id, date=date, VisitorType=VisitorType)
    if not visitor_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")
    return {"data": visitor_data}

# Ages Endpoint
@app.get("/ages/")
def get_age_groups(
    zone_id: str,
    date: date = Query(None),  # Accept date in YYYY-MM-DD format
    age_group: str = Query(None, alias="age_group"),
    db: Session = Depends(get_db)
):
    age_data = crud.get_age_groups(db, zone_id=zone_id, date=date, age_group=age_group)
    if not age_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")
    return {"data": age_data}

# Dwell Times Endpoint
@app.get("/dwell-times/")
def get_dwell_times(
    zone_id: str,
    date: date = Query(None),  # Accept date in YYYY-MM-DD format
    DwellTime: str = Query(None, alias="DwellTime"),
    db: Session = Depends(get_db)
):
    dwell_data = crud.get_dwell_times(db, zone_id=zone_id, date=date, DwellTime=DwellTime)
    if not dwell_data:
        raise HTTPException(status_code=404, detail="Data not found for the given parameters")
    return {"data": dwell_data}

# Daily Aggregated Endpoint
@app.get("/daily_aggregated/")
def get_daily_aggregated(
    zone_id: str,
    date: str = Query(None),  # Accept date in YYYY-MM-DD format
    date__gte: str = Query(None),
    date__lte: str = Query(None),
    db: Session = Depends(get_db)
):
    daily_data = crud.get_daily_aggregated(db, zone_id=zone_id, date=date, date__gte=date__gte, date__lte=date__lte)
    if not daily_data:
        raise HTTPException(status_code=404, detail="No data found for the given parameters.")
    return {"data": daily_data}

# Hourly Data Endpoint
@app.get("/daily/")
def get_hourly_data(
    zone_id: str,
    date__gte: str = Query(None),
    date__lte: str = Query(None),
    db: Session = Depends(get_db)
):
    if not date__gte or not date__lte:
        raise HTTPException(status_code=400, detail="Both date__gte and date__lte are required.")

    hourly_data = crud.get_hourly_aggregated(db, zone_id=zone_id, date__gte=date__gte, date__lte=date__lte)
    if not hourly_data:
        raise HTTPException(status_code=404, detail="No data found for the given parameters.")
    return {"data": hourly_data}

@app.get("/locations/all_summary/")
def get_all_summary(format: str = Query("json")):
    if format != "json":
        raise HTTPException(status_code=400, detail="Only 'json' format is supported.")

    # Adjust the path to reference the static folder one directory above
    file_path = os.path.join(os.path.dirname(__file__), "..", "static", "all_summary.json")
    file_path = os.path.abspath(file_path)  # Convert to an absolute path for safety

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Summary file not found.")

    return FileResponse(file_path)
