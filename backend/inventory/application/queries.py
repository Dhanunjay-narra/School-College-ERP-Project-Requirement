"""
Campus Inventory & Stores — CQRS Queries.
Defines read-model queries, filtering criteria, and sorting specifications for inventory.
"""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass(frozen=True)
class GetInventoryByIdQuery:
    id: str
    tenant_id: str = "default_institution"
    include_metadata: bool = True

@dataclass(frozen=True)
class ListInventorysQuery:
    tenant_id: str = "default_institution"
    status_filter: Optional[str] = None
    search_term: Optional[str] = None
    page: int = 1
    page_size: int = 20
    sort_by: str = "created_at"
    sort_desc: bool = True

@dataclass(frozen=True)
class CountInventorysQuery:
    tenant_id: str = "default_institution"
    status_filter: Optional[str] = None

@dataclass(frozen=True)
class SearchInventorysQuery:
    query: str
    tenant_id: str = "default_institution"
    facets: Optional[Dict[str, Any]] = None
    limit: int = 50
