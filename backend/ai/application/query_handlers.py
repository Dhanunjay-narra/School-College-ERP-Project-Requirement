"""
AI/ML Predictive Intelligence — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for ai.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.ai.domain.entities import AiEntity
from backend.ai.domain.repositories import IAiRepository
from backend.ai.application.queries import GetAiByIdQuery, ListAisQuery, CountAisQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.ai.query_handlers")

class AiQueryHandler:
    """Executes read-side CQRS queries for AI/ML Predictive Intelligence."""

    def __init__(self, repository: IAiRepository):
        self.repository = repository

    async def handle_get_by_id(self, query: GetAiByIdQuery) -> AiEntity:
        logger.debug(f"Executing GetAiByIdQuery for ID: {query.id}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("Ai", query.id)
        return entity

    async def handle_list(self, query: ListAisQuery) -> PaginatedResult[AiEntity]:
        logger.debug(f"Executing ListAisQuery for tenant: {query.tenant_id} (Page: {query.page})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: CountAisQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
