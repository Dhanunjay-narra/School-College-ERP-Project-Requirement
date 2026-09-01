"""
Transport Fleet, Routes, GPS Tracking & Stops API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/transport", tags=["Transportation Management"])

class BusRoute(BaseModel):
    route_id: str
    route_name: str
    bus_number: str
    driver_name: str
    driver_phone: str
    total_capacity: int
    assigned_students: int
    current_status: str
    live_lat: float
    live_lng: float

@router.get("/routes", response_model=List[BusRoute])
async def list_routes():
    return [
        BusRoute(route_id="RT-01", route_name="North Corridor - Tech Campus Express", bus_number="AP-29-BD-1001", driver_name="Gurpreet Singh", driver_phone="+91-9876541101", total_capacity=52, assigned_students=48, current_status="ON_ROUTE", live_lat=17.4400, live_lng=78.3489),
        BusRoute(route_id="RT-02", route_name="South City Ring Road Line", bus_number="AP-29-BD-1002", driver_name="Mahesh Yadav", driver_phone="+91-9876541102", total_capacity=52, assigned_students=44, current_status="AT_CAMPUS", live_lat=17.4455, live_lng=78.3520),
    ]
