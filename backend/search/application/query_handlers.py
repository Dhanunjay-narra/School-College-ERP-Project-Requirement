"""
Centralized Faceted Search — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for search.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.search.domain.entities import SearchEntity
from backend.search.domain.repositories import ISearchRepository
from backend.search.application.queries import GetSearchByIdQuery, ListSearchsQuery, CountSearchsQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.search.query_handlers")

class SearchQueryHandler:
    """Executes read-side CQRS queries for Centralized Faceted Search."""

    def __init__(self, repository: ISearchRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetSearchByIdQuery) -> SearchEntity:
        logger.debug(f"Executing GetSearchByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Search", query.id)
        return entity

    async def handle_list(self, query: ListSearchsQuery) -> PaginatedResult[SearchEntity]:
        logger.debug(f"Executing ListSearchsQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountSearchsQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
