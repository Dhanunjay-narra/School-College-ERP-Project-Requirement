"""
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
