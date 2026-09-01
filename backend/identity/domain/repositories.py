"""
Identity Domain Repository Interfaces.
"""
from abc import ABC, abstractmethod
from typing import Optional, List
from backend.identity.domain.entities import User, Role

class IUserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: str, tenant_id: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_email(self, email: str, tenant_id: str) -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user: User) -> User:
        pass

    @abstractmethod
    async def list_users(self, tenant_id: str, limit: int = 50, offset: int = 0) -> List[User]:
        pass

    @abstractmethod
    async def count(self, tenant_id: str) -> int:
        pass

class IRoleRepository(ABC):
    @abstractmethod
    async def get_by_id(self, role_id: str) -> Optional[Role]:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[Role]:
        pass

    @abstractmethod
    async def list_roles(self) -> List[Role]:
        pass

    @abstractmethod
    async def save(self, role: Role) -> Role:
        pass
