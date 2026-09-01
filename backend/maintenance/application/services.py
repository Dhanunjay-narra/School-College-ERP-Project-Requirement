"""
Campus Facility Maintenance — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.maintenance.domain.entities import MaintenanceEntity
from backend.maintenance.domain.repositories import IMaintenanceRepository
from backend.maintenance.domain.events import MaintenanceCreatedEvent, MaintenanceUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class MaintenanceService:
    def __init__(self, repo: IMaintenanceRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> MaintenanceEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = MaintenanceEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(MaintenanceCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> MaintenanceEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Maintenance", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[MaintenanceEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
