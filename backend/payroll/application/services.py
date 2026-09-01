"""
Integrated Payroll Engine — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.payroll.domain.entities import PayrollEntity
from backend.payroll.domain.repositories import IPayrollRepository
from backend.payroll.domain.events import PayrollCreatedEvent, PayrollUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class PayrollService:
    def __init__(self, repo: IPayrollRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> PayrollEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = PayrollEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(PayrollCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> PayrollEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Payroll", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[PayrollEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
