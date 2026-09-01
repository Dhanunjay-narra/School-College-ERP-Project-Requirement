"""
Encrypted Document Management & Verification API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/documents", tags=["Document Management"])

class DocumentRecord(BaseModel):
    id: str
    title: str
    document_type: str
    uploaded_by: str
    file_size_kb: int
    verification_status: str
    upload_date: str

@router.get("/", response_model=List[DocumentRecord])
async def list_documents():
    return [
        DocumentRecord(id="DOC-9901", title="Aarav_Patel_Class_12_Marksheet.pdf", document_type="ACADEMIC_CERTIFICATE", uploaded_by="Aarav Patel", file_size_kb=1240, verification_status="VERIFIED_AUTHENTIC", upload_date="2024-07-20"),
        DocumentRecord(id="DOC-9902", title="Institutional_NAAC_A++_Accreditation_Certificate.pdf", document_type="COMPLIANCE_LEGAL", uploaded_by="Principal Office", file_size_kb=4580, verification_status="VERIFIED_AUTHENTIC", upload_date="2023-11-15"),
    ]
