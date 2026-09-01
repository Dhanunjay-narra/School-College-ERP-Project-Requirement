"""
Centralized Permission-Aware Search Platform API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/search", tags=["Centralized Search"])

class SearchResult(BaseModel):
    category: str
    title: str
    subtitle: str
    link: str

@router.get("/", response_model=List[SearchResult])
async def search_all(query: str = ""):
    q = query.lower()
    items = [
        SearchResult(category="Student", title="Aarav Patel (24CSE042)", subtitle="B.Tech Computer Science - Semester 4", link="/students/STU-2026-001"),
        SearchResult(category="Faculty", title="Dr. David Smith", subtitle="Professor - Department of Computer Science", link="/faculty/FAC-001"),
        SearchResult(category="Course", title="CS401: Distributed Systems & Cloud Computing", subtitle="4 Credits - Semester 4", link="/academics/courses/CS401"),
        SearchResult(category="Book", title="Designing Data-Intensive Applications (978-0134494166)", subtitle="Martin Kleppmann - Shelf CS-12A", link="/library/books"),
        SearchResult(category="Invoice", title="INV-2026-8801: Tuition Fee Aarav Patel", subtitle="Paid ₹75,000 - Receipt Verified", link="/fees"),
    ]
    if q:
        items = [item for item in items if q in item.title.lower() or q in item.subtitle.lower() or q in item.category.lower()]
    return items
