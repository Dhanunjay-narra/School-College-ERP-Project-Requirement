"""
Organization API Endpoints.
"""
from fastapi import APIRouter, HTTPException
from typing import List
from backend.organization.presentation.schemas import InstitutionResponse, CampusResponse, DepartmentResponse, RoomResponse
from backend.organization.infrastructure.repositories import default_org_repo

router = APIRouter(prefix="/organization", tags=["Organization & Multi-Campus"])

@router.get("/institution", response_model=InstitutionResponse)
async def get_institution():
    """Get active institution details."""
    inst = await default_org_repo.get_institution("default_institution")
    if not inst:
        raise HTTPException(status_code=404, detail="Institution not found")
    return InstitutionResponse(
        id=inst.id,
        name=inst.name,
        code=inst.code,
        institution_type=inst.institution_type.value,
        accreditation=inst.accreditation,
        affiliation=inst.affiliation,
        currency=inst.currency,
        timezone=inst.timezone,
        contact_email=inst.contact_email,
        contact_phone=inst.contact_phone,
        address=inst.address
    )

@router.get("/campuses", response_model=List[CampusResponse])
async def list_campuses():
    """List institution campuses."""
    campuses = await default_org_repo.list_campuses("default_institution")
    return [
        CampusResponse(
            id=c.id,
            name=c.name,
            code=c.code,
            city=c.city,
            state=c.state,
            is_main_campus=c.is_main_campus
        )
        for c in campuses
    ]

@router.get("/departments", response_model=List[DepartmentResponse])
async def list_departments():
    """List academic and administrative departments."""
    depts = await default_org_repo.list_departments("default_institution")
    return [
        DepartmentResponse(
            id=d.id,
            name=d.name,
            code=d.code,
            department_type=d.department_type.value,
            email=d.email
        )
        for d in depts
    ]

@router.get("/rooms", response_model=List[RoomResponse])
async def list_rooms():
    """List campus facilities and classrooms."""
    rooms = await default_org_repo.list_rooms()
    return [
        RoomResponse(
            id=r.id,
            building_id=r.building_id,
            room_number=r.room_number,
            floor_number=r.floor_number,
            room_type=r.room_type.value,
            seating_capacity=r.seating_capacity,
            has_projector=r.has_projector,
            is_air_conditioned=r.is_air_conditioned
        )
        for r in rooms
    ]
