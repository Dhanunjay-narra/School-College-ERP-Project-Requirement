"""
Library MARC21/ISBN Catalog & RFID Circulation API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/library", tags=["Library Management"])

class LibraryBook(BaseModel):
    isbn: str
    title: str
    authors: str
    category: str
    total_copies: int
    available_copies: int
    shelf_location: str

@router.get("/books", response_model=List[LibraryBook])
async def list_books():
    return [
        LibraryBook(isbn="978-0134494166", title="Designing Data-Intensive Applications", authors="Martin Kleppmann", category="Computer Science", total_copies=12, available_copies=5, shelf_location="Shelf CS-12A"),
        LibraryBook(isbn="978-0262033848", title="Introduction to Algorithms (4th Edition)", authors="Cormen, Leiserson, Rivest, Stein", category="Algorithms", total_copies=25, available_copies=14, shelf_location="Shelf CS-04B"),
        LibraryBook(isbn="978-0132350884", title="Clean Code: A Handbook of Agile Software Craftsmanship", authors="Robert C. Martin", category="Software Engineering", total_copies=18, available_copies=8, shelf_location="Shelf CS-08C"),
    ]
