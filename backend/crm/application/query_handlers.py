"""
Institutional CRM & Admissions Leads — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for crm.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.crm.domain.entities import CrmEntity
from backend.crm.domain.repositories import ICrmRepository
from backend.crm.application.queries import GetCrmByIdQuery, ListCrmsQuery, CountCrmsQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.crm.query_handlers")

class CrmQueryHandler:
    """Executes read-side CQRS queries for Institutional CRM & Admissions Leads."""

    def __init__(self, repository: ICrmRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetCrmByIdQuery) -> CrmEntity:
        logger.debug(f"Executing GetCrmByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Crm", query.id)
        return entity

    async def handle_list(self, query: ListCrmsQuery) -> PaginatedResult[CrmEntity]:
        logger.debug(f"Executing ListCrmsQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountCrmsQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
