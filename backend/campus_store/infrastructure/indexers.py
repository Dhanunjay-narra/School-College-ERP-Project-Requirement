"""
Campus Store & Cafeteria POS — In-Memory Secondary Indexer.
Enables sub-millisecond lookup by code, status, and tenant in campus_store.
"""
from typing import Dict, List, Set, Optional
from backend.campus_store.domain.entities import CampusStoreEntity

class CampusStoreMemoryIndexer:
    """Secondary index manager for Campus Store & Cafeteria POS."""

    def __init__(self):
        self._code_index: Dict[str, str] = {}  # code -> id
        self._status_index: Dict[str, Set[str]] = {}  # status -> Set[id]
        self._tenant_index: Dict[str, Set[str]] = {}  # tenant_id -> Set[id]

    def index_entity(self, entity: CampusStoreEntity):
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
