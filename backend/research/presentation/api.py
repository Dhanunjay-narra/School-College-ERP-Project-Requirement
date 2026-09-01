"""
Research Projects, Grants, Publications & Patents API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/research", tags=["Research & Innovation Management"])

class ResearchGrant(BaseModel):
    grant_id: str
    project_title: str
    principal_investigator: str
    funding_agency: str
    sanctioned_amount: float
    disbursed_amount: float
    duration_months: int
    status: str

@router.get("/grants", response_model=List[ResearchGrant])
async def list_research_grants():
    return [
        ResearchGrant(grant_id="DST-SERB-2025-44", project_title="Edge AI for Smart Grid Energy Management", principal_investigator="Dr. David Smith", funding_agency="DST-SERB / Govt of India", sanctioned_amount=4500000.0, disbursed_amount=3000000.0, duration_months=36, status="IN_PROGRESS"),
        ResearchGrant(grant_id="ISRO-RESP-2025-12", project_title="Autonomous Satellite Imagery Analysis for Climate Tracking", principal_investigator="Prof. Ananya Iyer", funding_agency="ISRO / DOS", sanctioned_amount=6200000.0, disbursed_amount=4000000.0, duration_months=24, status="IN_PROGRESS"),
    ]
