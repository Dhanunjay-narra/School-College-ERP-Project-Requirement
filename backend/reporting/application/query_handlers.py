"""
Universal Enterprise Reporting — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for reporting.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.reporting.domain.entities import ReportingEntity
from backend.reporting.domain.repositories import IReportingRepository
from backend.reporting.application.queries import GetReportingByIdQuery, ListReportingsQuery, CountReportingsQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.reporting.query_handlers")

class ReportingQueryHandler:
    """Executes read-side CQRS queries for Universal Enterprise Reporting."""

    def __init__(self, repository: IReportingRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetReportingByIdQuery) -> ReportingEntity:
        logger.debug(f"Executing GetReportingByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Reporting", query.id)
        return entity

    async def handle_list(self, query: ListReportingsQuery) -> PaginatedResult[ReportingEntity]:
        logger.debug(f"Executing ListReportingsQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountReportingsQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
