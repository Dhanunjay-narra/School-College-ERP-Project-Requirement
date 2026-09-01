"""
Configurable Workflow & Multi-Tier Approval Engine API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/workflows", tags=["Workflow Approval Engine"])

class WorkflowRequest(BaseModel):
    workflow_id: str
    workflow_type: str
    initiator_name: str
    current_tier: str
    approver: str
    status: str
    submitted_at: str

@router.get("/pending", response_model=List[WorkflowRequest])
async def list_pending_workflows():
    return [
        WorkflowRequest(workflow_id="WF-REQ-801", workflow_type="Purchase Order > ₹100,000", initiator_name="Dr. David Smith", current_tier="Tier 3 (Principal Approval)", approver="Dr. Rajesh Sharma (Principal)", status="PENDING_APPROVAL", submitted_at="2026-08-29 11:20:00"),
        WorkflowRequest(workflow_id="WF-REQ-802", workflow_type="Faculty Medical Leave", initiator_name="Dr. Sarah Jenkins", current_tier="Tier 1 (HOD Approval)", approver="Prof. Ananya Iyer (HOD)", status="PENDING_APPROVAL", submitted_at="2026-08-31 08:45:00"),
    ]
