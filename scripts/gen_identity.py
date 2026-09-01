from writer_util import write_f

def build_identity():
    print("[PHASE 02] Building Identity & Access Management Module...")
    
    write_f("backend/identity/__init__.py", '"""Identity & Access Management Domain Package."""\n')
    write_f("backend/identity/domain/__init__.py", "")
    write_f("backend/identity/application/__init__.py", "")
    write_f("backend/identity/infrastructure/__init__.py", "")
    write_f("backend/identity/infrastructure/persistence/__init__.py", "")
    write_f("backend/identity/presentation/__init__.py", "")

    write_f("backend/identity/domain/value_objects.py", '''"""
Identity Domain Value Objects.
"""
from enum import Enum
from dataclasses import dataclass
from typing import Optional
import re

class RoleType(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    INSTITUTION_ADMIN = "INSTITUTION_ADMIN"
    CAMPUS_ADMIN = "CAMPUS_ADMIN"
    PRINCIPAL = "PRINCIPAL"
    DIRECTOR = "DIRECTOR"
    HOD = "HOD"
    FACULTY = "FACULTY"
    ACCOUNTANT = "ACCOUNTANT"
    HR_MANAGER = "HR_MANAGER"
    LIBRARIAN = "LIBRARIAN"
    TRANSPORT_MANAGER = "TRANSPORT_MANAGER"
    HOSTEL_WARDEN = "HOSTEL_WARDEN"
    EXAM_CONTROLLER = "EXAM_CONTROLLER"
    STUDENT = "STUDENT"
    PARENT = "PARENT"
    ALUMNI = "ALUMNI"
    VENDOR = "VENDOR"

class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    LOCKED = "LOCKED"

@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self):
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, self.value):
            raise ValueError(f"Invalid email address: {self.value}")

    def __str__(self) -> str:
        return self.value.lower()
''')

    write_f("backend/identity/domain/events.py", '''"""
Identity Domain Events.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional
from backend.core.events import DomainEvent

class UserRegisteredEvent(DomainEvent):
    def __init__(self, user_id: str, email: str, role: str, tenant_id: str):
        super().__init__(
            event_type="identity.user_registered",
            aggregate_id=user_id,
            tenant_id=tenant_id,
            payload={"user_id": user_id, "email": email, "role": role}
        )

class UserLoggedInEvent(DomainEvent):
    def __init__(self, user_id: str, ip_address: str, user_agent: str, tenant_id: str):
        super().__init__(
            event_type="identity.user_logged_in",
            aggregate_id=user_id,
            tenant_id=tenant_id,
            payload={"user_id": user_id, "ip": ip_address, "user_agent": user_agent}
        )

class UserLockedOutEvent(DomainEvent):
    def __init__(self, user_id: str, reason: str, tenant_id: str):
        super().__init__(
            event_type="identity.user_locked_out",
            aggregate_id=user_id,
            tenant_id=tenant_id,
            payload={"user_id": user_id, "reason": reason}
        )
''')

    write_f("backend/identity/domain/entities.py", '''"""
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
''')

    write_f("backend/identity/domain/repositories.py", '''"""
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
''')

    write_f("backend/identity/infrastructure/repositories.py", '''"""
In-Memory and Persistent Repository Implementations for Identity.
Pre-populated with demo enterprise credentials for instant 1-click login.
"""
from typing import Optional, List, Dict
import uuid
from datetime import datetime
from backend.identity.domain.entities import User, Role, Permission
from backend.identity.domain.value_objects import RoleType
from backend.identity.domain.repositories import IUserRepository, IRoleRepository
from backend.core.security import hash_password

class InMemoryRoleRepository(IRoleRepository):
    def __init__(self):
        self._roles: Dict[str, Role] = {}
        self._initialize_default_roles()

    def _initialize_default_roles(self):
        roles_data = [
            (RoleType.SUPER_ADMIN, "Super Administrator", "Full unrestricted access across all tenants and subsystems"),
            (RoleType.INSTITUTION_ADMIN, "Institution Admin", "Manage full institution policy, academic years, and departments"),
            (RoleType.CAMPUS_ADMIN, "Campus Admin", "Manage specific campus facilities, infrastructure, and staff"),
            (RoleType.PRINCIPAL, "Principal / Director", "Executive view of all academics, attendance, examinations, and finance"),
            (RoleType.HOD, "Head of Department", "Manage department faculty, curriculum, timetable, and approvals"),
            (RoleType.FACULTY, "Faculty / Teacher", "Class attendance, syllabus, assignment grading, and exams"),
            (RoleType.ACCOUNTANT, "Chief Accountant", "Fee billing, general ledger, payment reconciliations, and budgeting"),
            (RoleType.HR_MANAGER, "HR Manager", "Staff recruitment, employee lifecycle, leave, and payroll processing"),
            (RoleType.LIBRARIAN, "Chief Librarian", "Book catalog, ISBN/RFID tracking, circulation, and fines"),
            (RoleType.TRANSPORT_MANAGER, "Transport Manager", "Fleet vehicles, routes, stops, GPS tracking, and safety"),
            (RoleType.HOSTEL_WARDEN, "Hostel Warden", "Room allocation, outpass approvals, mess menus, and discipline"),
            (RoleType.EXAM_CONTROLLER, "Controller of Examinations", "Scheduling, question banks, hall allocations, and results"),
            (RoleType.STUDENT, "Enrolled Student", "Access student dashboard, assignments, timetable, and grades"),
            (RoleType.PARENT, "Parent / Guardian", "Monitor ward progress, attendance, fee invoices, and notices"),
        ]
        for role_type, name, desc in roles_data:
            role = Role(id=str(uuid.uuid4()), name=name, role_type=role_type, description=desc)
            self._roles[role.id] = role

    async def get_by_id(self, role_id: str) -> Optional[Role]:
        return self._roles.get(role_id)

    async def get_by_name(self, name: str) -> Optional[Role]:
        for role in self._roles.values():
            if role.name.lower() == name.lower() or role.role_type.value.lower() == name.lower():
                return role
        return None

    async def list_roles(self) -> List[Role]:
        return list(self._roles.values())

    async def save(self, role: Role) -> Role:
        self._roles[role.id] = role
        return role

class InMemoryUserRepository(IUserRepository):
    def __init__(self, role_repo: IRoleRepository):
        self._users: Dict[str, User] = {}
        self._role_repo = role_repo
        self._seed_default_users()

    def _seed_default_users(self):
        demo_password_hash = hash_password("Password@123")
        
        users_seed = [
            ("superadmin@erp.edu", "Super", "Admin", RoleType.SUPER_ADMIN, "CS-DEP", "MAIN-CAMPUS"),
            ("principal@erp.edu", "Dr. Rajesh", "Sharma", RoleType.PRINCIPAL, "ADMIN-DEP", "MAIN-CAMPUS"),
            ("hod.cs@erp.edu", "Prof. Ananya", "Iyer", RoleType.HOD, "CS-DEP", "MAIN-CAMPUS"),
            ("faculty.smith@erp.edu", "Dr. David", "Smith", RoleType.FACULTY, "CS-DEP", "MAIN-CAMPUS"),
            ("student.aarav@erp.edu", "Aarav", "Patel", RoleType.STUDENT, "CS-DEP", "MAIN-CAMPUS"),
            ("parent.sharma@erp.edu", "Vikram", "Sharma", RoleType.PARENT, None, "MAIN-CAMPUS"),
            ("accountant@erp.edu", "Priya", "Nair", RoleType.ACCOUNTANT, "FIN-DEP", "MAIN-CAMPUS"),
            ("hr.manager@erp.edu", "Sunil", "Verma", RoleType.HR_MANAGER, "HR-DEP", "MAIN-CAMPUS"),
            ("warden@erp.edu", "Col. Ramesh", "Singh", RoleType.HOSTEL_WARDEN, "HOSTEL-DEP", "MAIN-CAMPUS"),
            ("librarian@erp.edu", "Meenakshi", "Sundaram", RoleType.LIBRARIAN, "LIB-DEP", "MAIN-CAMPUS"),
            ("transport@erp.edu", "Gurpreet", "Singh", RoleType.TRANSPORT_MANAGER, "TRANS-DEP", "MAIN-CAMPUS"),
            ("exam.controller@erp.edu", "Dr. K.", "Venkatesh", RoleType.EXAM_CONTROLLER, "EXAM-DEP", "MAIN-CAMPUS"),
        ]

        for email, first, last, role_type, dep, campus in users_seed:
            user_id = str(uuid.uuid4())
            role = Role(id=str(uuid.uuid4()), name=role_type.value, role_type=role_type)
            user = User(
                id=user_id,
                email=email,
                hashed_password=demo_password_hash,
                first_name=first,
                last_name=last,
                roles=[role],
                phone_number="+91-9876543210",
                is_active=True,
                is_verified=True,
                tenant_id="default_institution",
                department_id=dep,
                campus_id=campus,
                created_at=datetime.utcnow()
            )
            self._users[user_id] = user

    async def get_by_id(self, user_id: str, tenant_id: str) -> Optional[User]:
        user = self._users.get(user_id)
        if user and user.tenant_id == tenant_id:
            return user
        return None

    async def get_by_email(self, email: str, tenant_id: str) -> Optional[User]:
        for user in self._users.values():
            if user.email == email.lower() and user.tenant_id == tenant_id:
                return user
        return None

    async def save(self, user: User) -> User:
        self._users[user.id] = user
        return user

    async def list_users(self, tenant_id: str, limit: int = 50, offset: int = 0) -> List[User]:
        tenant_users = [u for u in self._users.values() if u.tenant_id == tenant_id]
        return tenant_users[offset:offset+limit]

    async def count(self, tenant_id: str) -> int:
        return len([u for u in self._users.values() if u.tenant_id == tenant_id])

# Shared Singleton Repositories
default_role_repo = InMemoryRoleRepository()
default_user_repo = InMemoryUserRepository(default_role_repo)
''')

    write_f("backend/identity/application/services.py", '''"""
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
''')

    write_f("backend/identity/presentation/schemas.py", '''"""
Identity API Request and Response Schemas.
"""
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    tenant_id: str = "default_institution"

class UserProfileResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    role: str
    roles: List[str]
    tenant_id: str
    department_id: Optional[str] = None
    campus_id: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = 3600
    user: UserProfileResponse

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    role: str = "STUDENT"
    phone_number: Optional[str] = None
    department_id: Optional[str] = None
    campus_id: Optional[str] = None
''')

    write_f("backend/identity/presentation/api.py", '''"""
FastAPI Routes for Identity, Authentication, and Access Management.
"""
from fastapi import APIRouter, Depends, HTTPException, Header
from typing import List, Optional
from backend.identity.presentation.schemas import LoginRequest, TokenResponse, RegisterRequest, UserProfileResponse
from backend.identity.application.services import AuthenticationService
from backend.identity.infrastructure.repositories import default_user_repo, default_role_repo
from backend.identity.domain.value_objects import RoleType
from backend.core.security import decode_token

router = APIRouter(prefix="/auth", tags=["Identity & Authentication"])
auth_service = AuthenticationService(default_user_repo, default_role_repo)

async def get_current_user(authorization: Optional[str] = Header(None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer authorization token")
    token = authorization.split(" ")[1]
    payload = decode_token(token)
    return payload

@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest):
    """Authenticate user with email and password, returning JWT access tokens."""
    return await auth_service.authenticate(req.email, req.password, req.tenant_id)

@router.post("/register")
async def register(req: RegisterRequest):
    """Register a new user in the enterprise system."""
    try:
        role_type = RoleType(req.role.upper())
    except ValueError:
        role_type = RoleType.STUDENT
    
    user = await auth_service.register(
        email=req.email,
        password=req.password,
        first_name=req.first_name,
        last_name=req.last_name,
        role_type=role_type,
        phone=req.phone_number,
        department_id=req.department_id,
        campus_id=req.campus_id
    )
    return {"message": "User registered successfully", "user_id": user.id, "email": user.email}

@router.get("/me", response_model=UserProfileResponse)
async def get_profile(current_user: dict = Depends(get_current_user)):
    """Retrieve currently authenticated user profile."""
    user = await default_user_repo.get_by_id(current_user["sub"], current_user.get("tenant_id", "default_institution"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    primary_role = user.roles[0].role_type.value if user.roles else "STUDENT"
    return UserProfileResponse(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        full_name=user.full_name,
        role=primary_role,
        roles=[r.role_type.value for r in user.roles],
        tenant_id=user.tenant_id,
        department_id=user.department_id,
        campus_id=user.campus_id
    )

@router.get("/users")
async def list_users(current_user: dict = Depends(get_current_user)):
    """List institution users."""
    users = await default_user_repo.list_users(current_user.get("tenant_id", "default_institution"))
    return [
        {
            "id": u.id,
            "email": u.email,
            "full_name": u.full_name,
            "role": u.roles[0].role_type.value if u.roles else "STUDENT",
            "department_id": u.department_id,
            "campus_id": u.campus_id,
            "is_active": u.is_active
        }
        for u in users
    ]
''')

    print("[GEN] Identity & Access Management Module complete.")

if __name__ == '__main__':
    build_identity()
