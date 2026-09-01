"""
Identity Domain Entities.
"""
from datetime import datetime
from typing import List, Optional, Set
import uuid
from backend.identity.domain.value_objects import RoleType, SessionStatus

class Permission:
    def __init__(self, code: str, name: str, description: str, resource: str, action: str):
        self.code = code
        self.name = name
        self.description = description
        self.resource = resource
        self.action = action

class Role:
    def __init__(self, id: str, name: str, role_type: RoleType, description: str = "", permissions: Optional[List[Permission]] = None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.role_type = role_type
        self.description = description
        self.permissions: List[Permission] = permissions or []

    def add_permission(self, permission: Permission):
        if not any(p.code == permission.code for p in self.permissions):
            self.permissions.append(permission)

    def has_permission(self, permission_code: str) -> bool:
        return any(p.code == permission_code for p in self.permissions)

class User:
    def __init__(
        self,
        id: str,
        email: str,
        hashed_password: str,
        first_name: str,
        last_name: str,
        roles: Optional[List[Role]] = None,
        phone_number: Optional[str] = None,
        is_active: bool = True,
        is_verified: bool = False,
        mfa_enabled: bool = False,
        mfa_secret: Optional[str] = None,
        tenant_id: str = "default_institution",
        department_id: Optional[str] = None,
        campus_id: Optional[str] = None,
        failed_login_attempts: int = 0,
        locked_until: Optional[datetime] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id or str(uuid.uuid4())
        self.email = email.lower()
        self.hashed_password = hashed_password
        self.first_name = first_name
        self.last_name = last_name
        self.roles: List[Role] = roles or []
        self.phone_number = phone_number
        self.is_active = is_active
        self.is_verified = is_verified
        self.mfa_enabled = mfa_enabled
        self.mfa_secret = mfa_secret
        self.tenant_id = tenant_id
        self.department_id = department_id
        self.campus_id = campus_id
        self.failed_login_attempts = failed_login_attempts
        self.locked_until = locked_until
        self.created_at = created_at or datetime.utcnow()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def is_locked(self) -> bool:
        if self.locked_until and self.locked_until > datetime.utcnow():
            return True
        return False

    def record_login_failure(self, max_attempts: int = 5, lock_minutes: int = 15):
        self.failed_login_attempts += 1
        if self.failed_login_attempts >= max_attempts:
            from datetime import timedelta
            self.locked_until = datetime.utcnow() + timedelta(minutes=lock_minutes)

    def record_login_success(self):
        self.failed_login_attempts = 0
        self.locked_until = None

    def has_role(self, role_type: RoleType) -> bool:
        return any(r.role_type == role_type for r in self.roles)

    def has_permission(self, permission_code: str) -> bool:
        if self.has_role(RoleType.SUPER_ADMIN):
            return True
        for role in self.roles:
            if role.has_permission(permission_code):
                return True
        return False
