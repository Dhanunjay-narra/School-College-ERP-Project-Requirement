"""
Pagination, Filtering, and Sorting Helpers.
"""
from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel, Field

T = TypeVar("T")

class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1, description="Page number")
    page_size: int = Field(default=20, ge=1, le=100, description="Items per page")
    sort_by: Optional[str] = Field(default="created_at", description="Field to sort by")
    sort_desc: bool = Field(default=True, description="Sort descending")
    search: Optional[str] = Field(default=None, description="Search query string")

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

class PaginatedResult(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool

    @classmethod
    def create(cls, items: List[T], total: int, params: PaginationParams) -> "PaginatedResult[T]":
        total_pages = (total + params.page_size - 1) // params.page_size if total > 0 else 1
        return cls(
            items=items,
            total=total,
            page=params.page,
            page_size=params.page_size,
            total_pages=total_pages,
            has_next=params.page < total_pages,
            has_prev=params.page > 1
        )
