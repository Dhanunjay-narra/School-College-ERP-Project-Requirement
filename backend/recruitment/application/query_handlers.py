"""
Applicant Tracking System — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for recruitment.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.recruitment.domain.entities import RecruitmentEntity
from backend.recruitment.domain.repositories import IRecruitmentRepository
from backend.recruitment.application.queries import GetRecruitmentByIdQuery, ListRecruitmentsQuery, CountRecruitmentsQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.recruitment.query_handlers")

class RecruitmentQueryHandler:
    """Executes read-side CQRS queries for Applicant Tracking System."""

    def __init__(self, repository: IRecruitmentRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetRecruitmentByIdQuery) -> RecruitmentEntity:
        logger.debug(f"Executing GetRecruitmentByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Recruitment", query.id)
        return entity

    async def handle_list(self, query: ListRecruitmentsQuery) -> PaginatedResult[RecruitmentEntity]:
        logger.debug(f"Executing ListRecruitmentsQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountRecruitmentsQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
