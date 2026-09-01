"""
Assignments & Learning Management System API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/assignments", tags=["Assignments & LMS"])

class Assignment(BaseModel):
    id: str
    title: str
    subject: str
    due_date: str
    max_marks: int
    status: str
    submission_count: int

@router.get("/", response_model=List[Assignment])
async def list_assignments():
    return [
        Assignment(id="ASN-001", title="Raft Consensus Algorithm Implementation", subject="Distributed Systems (CS401)", due_date="2026-09-10", max_marks=50, status="SUBMITTED", submission_count=42),
        Assignment(id="ASN-002", title="Convolutional Neural Network for Image Recognition", subject="Artificial Intelligence (CS402)", due_date="2026-09-14", max_marks=100, status="PENDING", submission_count=28),
        Assignment(id="ASN-003", title="B-Tree Indexing Optimization", subject="Database Engineering (CS403)", due_date="2026-09-20", max_marks=50, status="GRADED", submission_count=45),
    ]
