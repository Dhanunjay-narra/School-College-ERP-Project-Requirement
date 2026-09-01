"""
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
