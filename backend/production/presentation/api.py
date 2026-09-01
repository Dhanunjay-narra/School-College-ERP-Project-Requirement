"""
Campus Engineering Workshop & Fab Lab Production API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/production", tags=["Campus Workshop & Fabrication"])

class WorkshopWorkOrder(BaseModel):
    order_id: str
    project_title: str
    department: str
    materials_used: str
    status: str
    estimated_cost: float

@router.get("/work-orders", response_model=List[WorkshopWorkOrder])
async def list_work_orders():
    return [
        WorkshopWorkOrder(order_id="WO-2026-101", project_title="Autonomous Drone Chassis 3D Fabrication", department="Robotics & CSE", materials_used="Carbon Fiber Filament, PLA", status="COMPLETED", estimated_cost=4500.0),
        WorkshopWorkOrder(order_id="WO-2026-102", project_title="Solar Tracking Motor Prototype Housing", department="Mechanical Engineering", materials_used="Aluminium 6061 Block, Fasteners", status="IN_PRODUCTION", estimated_cost=12500.0),
    ]
