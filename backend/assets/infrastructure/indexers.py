"""
Asset Lifecycle & Depreciation — In-Memory Secondary Indexer.
Enables sub-millisecond lookup by code, status, and tenant in assets.
"""
from typing import Dict, List, Set, Optional
from backend.assets.domain.entities import AssetsEntity

class AssetsMemoryIndexer:
    """Secondary index manager for Asset Lifecycle & Depreciation."""

    def __init__(self):
        self._code_index: Dict[str, str] = {}  # code -> id
        self._status_index: Dict[str, Set[str]] = {}  # status -> Set[id]
        self._tenant_index: Dict[str, Set[str]] = {}  # tenant_id -> Set[id]

    def index_entity(self, entity: AssetsEntity):
        self._code_index[f"{entity.tenant_id}:{entity.code.upper()}"] = entity.id
        
        status_key = entity.status.upper()
        if status_key not in self._status_index:
            self._status_index[status_key] = set()
        self._status_index[status_key].add(entity.id)

        if entity.tenant_id not in self._tenant_index:
            self._tenant_index[entity.tenant_id] = set()
        self._tenant_index[entity.tenant_id].add(entity.id)

    def find_id_by_code(self, tenant_id: str, code: str) -> Optional[str]:
        return self._code_index.get(f"{tenant_id}:{code.upper()}")

    def find_ids_by_status(self, status: str) -> Set[str]:
        return self._status_index.get(status.upper(), set())
