"""
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
