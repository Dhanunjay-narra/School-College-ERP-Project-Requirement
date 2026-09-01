"""
Accreditation & Regulatory Compliance — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for compliance.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.compliance.domain.entities import ComplianceEntity
from backend.compliance.domain.repositories import IComplianceRepository
from backend.compliance.application.queries import GetComplianceByIdQuery, ListCompliancesQuery, CountCompliancesQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.compliance.query_handlers")

class ComplianceQueryHandler:
    """Executes read-side CQRS queries for Accreditation & Regulatory Compliance."""

    def __init__(self, repository: IComplianceRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetComplianceByIdQuery) -> ComplianceEntity:
        logger.debug(f"Executing GetComplianceByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Compliance", query.id)
        return entity

    async def handle_list(self, query: ListCompliancesQuery) -> PaginatedResult[ComplianceEntity]:
        logger.debug(f"Executing ListCompliancesQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountCompliancesQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
