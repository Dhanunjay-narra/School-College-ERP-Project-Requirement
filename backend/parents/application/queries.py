"""
Parent & Guardian Management — CQRS Queries.
Defines read-model queries, filtering criteria, and sorting specifications for parents.
"""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass(frozen=True)
class GetParentsByIdQuery:
    id: str
    tenant_id: str = "default_institution"
    include_metadata: bool = True

@dataclass(frozen=True)
class ListParentssQuery:
    tenant_id: str = "default_institution"
    status_filter: Optional[str] = None
    search_term: Optional[str] = None
    page: int = 1
    page_size: int = 20
    sort_by: str = "created_at"
    sort_desc: bool = True

@dataclass(frozen=True)
class CountParentssQuery:
    tenant_id: str = "default_institution"
    status_filter: Optional[str] = None

@dataclass(frozen=True)
class SearchParentssQuery:
    query: str
    tenant_id: str = "default_institution"
    facets: Optional[Dict[str, Any]] = None
    limit: int = 50
