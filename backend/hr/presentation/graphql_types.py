"""
Human Resource & Recruitment — GraphQL Type Definitions & Resolvers.
Provides federated GraphQL schema mappings for hr.
"""
from typing import Optional, List, Dict, Any

class HrGraphQLType:
    """GraphQL Object Type for Hr."""
    def __init__(self, id: str, code: str, name: str, status: str, tenant_id: str):
        self.id = id
        self.code = code
        self.name = name
        self.status = status
        self.tenant_id = tenant_id

    @classmethod
    def from_entity(cls, entity) -> "HrGraphQLType":
        return cls(
            id=entity.id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            tenant_id=entity.tenant_id
        )

    def resolve_display_label(self) -> str:
        return f"[{self.code}] {self.name} ({self.status})"
