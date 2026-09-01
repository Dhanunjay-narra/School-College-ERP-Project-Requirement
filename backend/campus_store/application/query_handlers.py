"""
Campus Store & Cafeteria POS — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for campus_store.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.domain.repositories import ICampusStoreRepository
from backend.campus_store.application.queries import GetCampusStoreByIdQuery, ListCampusStoresQuery, CountCampusStoresQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.campus_store.query_handlers")

class CampusStoreQueryHandler:
    """Executes read-side CQRS queries for Campus Store & Cafeteria POS."""

    def __init__(self, repository: ICampusStoreRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetCampusStoreByIdQuery) -> CampusStoreEntity:
        logger.debug(f"Executing GetCampusStoreByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("CampusStore", query.id)
        return entity

    async def handle_list(self, query: ListCampusStoresQuery) -> PaginatedResult[CampusStoreEntity]:
        logger.debug(f"Executing ListCampusStoresQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountCampusStoresQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
