"""
Identity Application Services: Authentication, Authorization, and User Management.
"""
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from backend.identity.domain.entities import User, Role
from backend.identity.domain.value_objects import RoleType
from backend.identity.domain.repositories import IUserRepository, IRoleRepository
from backend.identity.domain.events import UserRegisteredEvent, UserLoggedInEvent
from backend.core.security import (
    verify_password,
    hash_password,
    create_access_token,
    create_refresh_token,
    validate_password_strength,
    verify_totp,
    generate_totp_secret
)
from backend.core.exceptions import (
    UnauthorizedException,
    ForbiddenException,
    ConflictException,
    EntityNotFoundException,
    ValidationException
)
from backend.core.events import event_bus

class AuthenticationService:
    def __init__(self, user_repo: IUserRepository, role_repo: IRoleRepository):
        self.user_repo = user_repo
        self.role_repo = role_repo

    async def authenticate(self, email: str, password: str, tenant_id: str = "default_institution", ip_address: str = "127.0.0.1") -> Dict[str, Any]:
        user = await self.user_repo.get_by_email(email, tenant_id)
        if not user:
            raise UnauthorizedException("Invalid email address or password")

        if user.is_locked():
            raise ForbiddenException(f"Account locked until {user.locked_until}. Please try again later.")

        if not user.is_active:
            raise ForbiddenException("Your account is deactivated. Please contact the administrator.")

        if not verify_password(password, user.hashed_password):
            user.record_login_failure()
            await self.user_repo.save(user)
            raise UnauthorizedException("Invalid email address or password")

        user.record_login_success()
        await self.user_repo.save(user)

        # Dispatch login event
        await event_bus.publish(UserLoggedInEvent(user.id, ip_address, "Web Browser", tenant_id))

        primary_role = user.roles[0].role_type.value if user.roles else "STUDENT"
        access_token = create_access_token({
            "sub": user.id,
            "email": user.email,
            "roles": [r.role_type.value for r in user.roles],
            "tenant_id": user.tenant_id,
            "department_id": user.department_id,
            "campus_id": user.campus_id,
            "name": user.full_name
        })
        refresh_token = create_refresh_token({"sub": user.id, "tenant_id": user.tenant_id})

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": 3600,
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "full_name": user.full_name,
                "role": primary_role,
                "roles": [r.role_type.value for r in user.roles],
                "tenant_id": user.tenant_id,
                "department_id": user.department_id,
                "campus_id": user.campus_id
            }
        }

    async def register(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        role_type: RoleType = RoleType.STUDENT,
        phone: Optional[str] = None,
        tenant_id: str = "default_institution",
        department_id: Optional[str] = None,
        campus_id: Optional[str] = None
    ) -> User:
        existing = await self.user_repo.get_by_email(email, tenant_id)
        if existing:
            raise ConflictException(f"User with email '{email}' already registered.")

        if not validate_password_strength(password):
            raise ValidationException("Password does not meet enterprise complexity requirements.")

        role = await self.role_repo.get_by_name(role_type.value)
        if not role:
            role = Role(id="", name=role_type.value, role_type=role_type)

        user = User(
            id="",
            email=email,
            hashed_password=hash_password(password),
            first_name=first_name,
            last_name=last_name,
            roles=[role],
            phone_number=phone,
            tenant_id=tenant_id,
            department_id=department_id,
            campus_id=campus_id
        )

        saved = await self.user_repo.save(user)
        await event_bus.publish(UserRegisteredEvent(saved.id, saved.email, role_type.value, tenant_id))
        return saved
