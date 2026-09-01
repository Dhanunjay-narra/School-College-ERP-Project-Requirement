"""
Organization & Multi-Campus — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for organization.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.organization.domain.entities import OrganizationEntity
from backend.organization.domain.repositories import IOrganizationRepository
from backend.organization.application.queries import GetOrganizationByIdQuery, ListOrganizationsQuery, CountOrganizationsQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.organization.query_handlers")

class OrganizationQueryHandler:
    """Executes read-side CQRS queries for Organization & Multi-Campus."""

    def __init__(self, repository: IOrganizationRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetOrganizationByIdQuery) -> OrganizationEntity:
        logger.debug(f"Executing GetOrganizationByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Organization", query.id)
        return entity

    async def handle_list(self, query: ListOrganizationsQuery) -> PaginatedResult[OrganizationEntity]:
        logger.debug(f"Executing ListOrganizationsQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountOrganizationsQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
