"""
Compliance, Accreditation & Immutable Audit Log API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/compliance", tags=["Compliance & Audit"])

class AuditLogEntry(BaseModel):
    id: str
    timestamp: str
    actor_email: str
    action: str
    entity_type: str
    entity_id: str
    ip_address: str
    status: str

@router.get("/audit-logs", response_model=List[AuditLogEntry])
async def list_audit_logs():
    return [
        AuditLogEntry(id="AUD-8801", timestamp="2026-08-31 16:45:12", actor_email="superadmin@erp.edu", action="UPDATE_POLICY", entity_type="INSTITUTION_POLICY", entity_id="default_institution", ip_address="192.168.1.10", status="SUCCESS"),
        AuditLogEntry(id="AUD-8802", timestamp="2026-08-31 15:30:20", actor_email="accountant@erp.edu", action="APPROVE_FEE_RECEIPT", entity_type="FEE_INVOICE", entity_id="INV-2026-8801", ip_address="192.168.1.15", status="SUCCESS"),
        AuditLogEntry(id="AUD-8803", timestamp="2026-08-31 14:10:05", actor_email="faculty.smith@erp.edu", action="RECORD_ATTENDANCE", entity_type="ATTENDANCE_SESSION", entity_id="ATT-CS401-20260831", ip_address="192.168.1.42", status="SUCCESS"),
    ]
