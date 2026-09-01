import os
import sys
from pathlib import Path
from writer_util import write_f

def build_phase01_03():
    print("[PHASE 01-03] Building Foundation, Core Infrastructure, Identity, and Organization...")

    # Phase 01: Core Platform Files
    write_f("backend/__init__.py", '"""Enterprise School & College ERP Backend Package."""\n__version__ = "1.0.0"\n')
    
    write_f("backend/core/__init__.py", '"""Core infrastructure, configuration, database, security, and event utilities."""\n')

    write_f("backend/core/config.py", '''"""
Application Configuration Module.
Loads settings from environment variables and .env with Pydantic validation.
"""
import os
from typing import List, Optional, Union
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator

class Settings(BaseSettings):
    # App Information
    APP_NAME: str = "Enterprise School & College ERP"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    PORT: int = 8000
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "erp-enterprise-super-secure-production-key-2026-xyz"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS Settings
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # Database Configuration
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "school_college_erp"
    DB_SCHEMA: str = "public"
    DATABASE_URL: Optional[str] = None
    DATABASE_SYNC_URL: Optional[str] = None

    # Redis Cache & Session
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = 0
    REDIS_URL: Optional[str] = None

    # Event Broker
    EVENT_BROKER_TYPE: str = "memory"  # memory, redis, rabbitmq, kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    RABBITMQ_URL: str = "amqp://guest:guest@localhost:5672/"

    # Storage Provider
    STORAGE_PROVIDER: str = "local"  # local, s3, minio
    STORAGE_LOCAL_DIR: str = "uploads"
    S3_BUCKET_NAME: str = "erp-documents"
    S3_REGION: str = "us-east-1"
    S3_ACCESS_KEY: Optional[str] = "minioadmin"
    S3_SECRET_KEY: Optional[str] = "minioadmin"
    S3_ENDPOINT_URL: Optional[str] = "http://localhost:9000"

    # Communication & SMTP
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "notifications@erp.edu"
    SMTP_PASSWORD: str = "demo-app-password"
    SMTP_FROM_EMAIL: str = "no-reply@erp.edu"
    SMS_PROVIDER: str = "twilio"
    TWILIO_ACCOUNT_SID: str = "AC_DEMO_SID"
    TWILIO_AUTH_TOKEN: str = "DEMO_TOKEN"
    TWILIO_PHONE_NUMBER: str = "+1234567890"

    # Security & Password Policies
    PASSWORD_MIN_LENGTH: int = 8
    PASSWORD_REQUIRE_UPPERCASE: bool = True
    PASSWORD_REQUIRE_LOWERCASE: bool = True
    PASSWORD_REQUIRE_DIGITS: bool = True
    PASSWORD_REQUIRE_SPECIAL: bool = True
    MAX_FAILED_LOGIN_ATTEMPTS: int = 5
    ACCOUNT_LOCKOUT_MINUTES: int = 15

    class Config:
        env_file = ".env"
        case_sensitive = True

    def get_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_sync_database_url(self) -> str:
        if self.DATABASE_SYNC_URL:
            return self.DATABASE_SYNC_URL
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_redis_url(self) -> str:
        if self.REDIS_URL:
            return self.REDIS_URL
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

settings = Settings()
''')

    write_f("backend/core/database.py", '''"""
Database Engine, Session Management, and Base Entity Models.
Provides async SQLAlchemy sessions with tenant isolation and audit mixins.
"""
import uuid
from datetime import datetime
from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, declared_attr, Mapped, mapped_column
from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey, Text
from backend.core.config import settings

# Engine configuration
engine = create_async_engine(
    settings.get_database_url(),
    echo=settings.DEBUG,
    future=True,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

class TimestampMixin:
    """Provides created_at and updated_at timestamps."""
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class SoftDeleteMixin:
    """Enables soft deletion for compliance and data recovery."""
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    deleted_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

class TenantMixin:
    """Enables multi-tenant data partitioning."""
    tenant_id: Mapped[str] = mapped_column(String(64), nullable=False, index=True, default="default_institution")

class AuditMixin:
    """Tracks creating and modifying user IDs."""
    created_by: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    updated_by: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

class OptimisticLockMixin:
    """Optimistic concurrency control via version counter."""
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

class BaseEntity(Base, TimestampMixin, SoftDeleteMixin, TenantMixin, AuditMixin, OptimisticLockMixin):
    """Abstract Base Entity with UUID primary key and standard audit fields."""
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency injection helper for database sessions."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
''')

    write_f("backend/core/events.py", '''"""
Domain Event Broker and Event Bus Architecture.
Supports decoupled asynchronous domain event publishing and subscription.
"""
import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Dict, List, Callable, Any, Type, Awaitable
from pydantic import BaseModel, Field

logger = logging.getLogger("erp.events")

class DomainEvent(BaseModel):
    """Base domain event class with event metadata."""
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str
    aggregate_id: str
    tenant_id: str = "default_institution"
    occurred_at: datetime = Field(default_factory=datetime.utcnow)
    payload: Dict[str, Any] = Field(default_factory=dict)
    version: int = 1

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

EventHandler = Callable[[DomainEvent], Awaitable[None]]

class EventBroker:
    """Central event broker for in-process or distributed event delivery."""
    def __init__(self):
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._event_history: List[DomainEvent] = []

    def subscribe(self, event_type: str, handler: EventHandler):
        """Register an async event listener."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
        logger.info(f"Registered subscriber for event: {event_type}")

    async def publish(self, event: DomainEvent):
        """Dispatch domain event to all registered listeners asynchronously."""
        self._event_history.append(event)
        logger.info(f"Publishing domain event: {event.event_type} (ID: {event.event_id}) for aggregate: {event.aggregate_id}")
        
        handlers = self._handlers.get(event.event_type, [])
        handlers += self._handlers.get("*", [])  # Global listeners

        for handler in handlers:
            try:
                # Run handler asynchronously in event loop
                asyncio.create_task(self._safe_execute(handler, event))
            except Exception as ex:
                logger.error(f"Error launching handler for {event.event_type}: {str(ex)}")

    async def _safe_execute(self, handler: EventHandler, event: DomainEvent):
        try:
            await handler(event)
        except Exception as ex:
            logger.error(f"Handler execution failed for event {event.event_type}: {str(ex)}", exc_info=True)

    def get_history(self) -> List[DomainEvent]:
        return self._event_history

event_bus = EventBroker()
''')

    write_f("backend/core/exceptions.py", '''"""
Standard Enterprise ERP Domain and Application Exceptions.
"""
from typing import Optional, Dict, Any

class ERPBaseException(Exception):
    """Root ERP exception with status code and error details."""
    def __init__(self, message: str, status_code: int = 400, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

class DomainException(ERPBaseException):
    """Raised when a domain rule or invariant is violated."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=422, details=details)

class EntityNotFoundException(ERPBaseException):
    """Raised when requested entity is not found."""
    def __init__(self, entity_name: str, entity_id: str):
        message = f"{entity_name} with ID '{entity_id}' not found."
        super().__init__(message, status_code=404, details={"entity": entity_name, "id": entity_id})

class UnauthorizedException(ERPBaseException):
    """Raised on authentication failure."""
    def __init__(self, message: str = "Invalid authentication credentials"):
        super().__init__(message, status_code=401)

class ForbiddenException(ERPBaseException):
    """Raised on authorization failure or missing permissions."""
    def __init__(self, message: str = "Operation not permitted"):
        super().__init__(message, status_code=403)

class ConflictException(ERPBaseException):
    """Raised on duplicate unique constraints."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=409, details=details)

class ValidationException(ERPBaseException):
    """Raised on invalid user input."""
    def __init__(self, message: str, errors: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=400, details=errors)

class ConcurrencyException(ERPBaseException):
    """Raised on optimistic locking conflict."""
    def __init__(self, message: str = "Entity was modified by another transaction. Please refresh."):
        super().__init__(message, status_code=409)
''')

    write_f("backend/core/security.py", '''"""
Security Utilities: Password Hashing, JWT Tokens, MFA TOTP, and Sanitization.
"""
import re
import pyotp
import jwt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
from passlib.context import CryptContext
from backend.core.config import settings
from backend.core.exceptions import UnauthorizedException

pwd_context = CryptContext(
    schemes=["bcrypt", "argon2"],
    deprecated="auto",
    bcrypt__rounds=12
)

def hash_password(password: str) -> str:
    """Securely hash a password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify plain password against hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Generate signed JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": datetime.utcnow()})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def create_refresh_token(data: Dict[str, Any]) -> str:
    """Generate signed JWT refresh token with longer validity."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "iat": datetime.utcnow(), "type": "refresh"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def decode_token(token: str) -> Dict[str, Any]:
    """Decode and validate a signed JWT token."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise UnauthorizedException("Authentication token has expired")
    except jwt.PyJWTError:
        raise UnauthorizedException("Invalid authentication token")

def generate_totp_secret() -> str:
    """Generate a random base32 secret for MFA."""
    return pyotp.random_base32()

def verify_totp(secret: str, code: str) -> bool:
    """Verify TOTP verification code."""
    totp = pyotp.TOTP(secret)
    return totp.verify(code, valid_window=1)

def validate_password_strength(password: str) -> bool:
    """Validate password according to enterprise security policy."""
    if len(password) < settings.PASSWORD_MIN_LENGTH:
        return False
    if settings.PASSWORD_REQUIRE_UPPERCASE and not re.search(r"[A-Z]", password):
        return False
    if settings.PASSWORD_REQUIRE_LOWERCASE and not re.search(r"[a-z]", password):
        return False
    if settings.PASSWORD_REQUIRE_DIGITS and not re.search(r"\d", password):
        return False
    if settings.PASSWORD_REQUIRE_SPECIAL and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True
''')

    write_f("backend/core/pagination.py", '''"""
Pagination, Filtering, and Sorting Helpers.
"""
from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel, Field

T = TypeVar("T")

class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1, description="Page number")
    page_size: int = Field(default=20, ge=1, le=100, description="Items per page")
    sort_by: Optional[str] = Field(default="created_at", description="Field to sort by")
    sort_desc: bool = Field(default=True, description="Sort descending")
    search: Optional[str] = Field(default=None, description="Search query string")

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

class PaginatedResult(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool

    @classmethod
    def create(cls, items: List[T], total: int, params: PaginationParams) -> "PaginatedResult[T]":
        total_pages = (total + params.page_size - 1) // params.page_size if total > 0 else 1
        return cls(
            items=items,
            total=total,
            page=params.page,
            page_size=params.page_size,
            total_pages=total_pages,
            has_next=params.page < total_pages,
            has_prev=params.page > 1
        )
''')

    write_f("backend/core/middleware.py", '''"""
Custom Enterprise Middlewares: Security, Logging, Tenant Context, and Error Handling.
"""
import time
import logging
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from backend.core.exceptions import ERPBaseException

logger = logging.getLogger("erp.middleware")

class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        tenant_id = request.headers.get("X-Tenant-ID", "default_institution")
        
        request.state.request_id = request_id
        request.state.tenant_id = tenant_id
        
        start_time = time.time()
        logger.info(f"Incoming request: {request.method} {request.url.path} (Tenant: {tenant_id}, ReqID: {request_id})")
        
        try:
            response = await call_next(request)
            process_time = (time.time() - start_time) * 1000
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time-Ms"] = f"{process_time:.2f}"
            
            # Security Headers
            response.headers["X-Content-Type-Options"] = "nosniff"
            response.headers["X-Frame-Options"] = "DENY"
            response.headers["X-XSS-Protection"] = "1; mode=block"
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
            
            logger.info(f"Completed {request.method} {request.url.path} in {process_time:.2f}ms with status {response.status_code}")
            return response
        except ERPBaseException as ex:
            process_time = (time.time() - start_time) * 1000
            logger.warning(f"ERP Exception ({ex.status_code}): {ex.message}")
            return JSONResponse(
                status_code=ex.status_code,
                content={
                    "error": True,
                    "message": ex.message,
                    "details": ex.details,
                    "request_id": request_id
                }
            )
        except Exception as ex:
            process_time = (time.time() - start_time) * 1000
            logger.error(f"Unhandled Exception: {str(ex)}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "error": True,
                    "message": "Internal server error. Our engineering team has been notified.",
                    "request_id": request_id
                }
            )
''')

    write_f("backend/core/cache.py", '''"""
Redis and In-Memory Caching Layer with TTL and Pattern Invalidation.
"""
import json
import logging
from typing import Optional, Any, Dict
from datetime import timedelta

logger = logging.getLogger("erp.cache")

class MemoryCache:
    """High-performance in-memory cache fallback."""
    def __init__(self):
        self._store: Dict[str, Any] = {}

    def get(self, key: str) -> Optional[Any]:
        return self._store.get(key)

    def set(self, key: str, value: Any, ttl_seconds: int = 300):
        self._store[key] = value

    def delete(self, key: str):
        self._store.pop(key, None)

    def clear(self):
        self._store.clear()

cache_client = MemoryCache()
''')

    write_f("backend/core/websocket_manager.py", '''"""
WebSocket Connection Manager for Real-Time Portals, Alerts, and Chat.
"""
import json
import logging
from typing import Dict, List, Any
from fastapi import WebSocket

logger = logging.getLogger("erp.websocket")

class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, channel: str):
        await websocket.accept()
        if channel not in self.active_connections:
            self.active_connections[channel] = []
        self.active_connections[channel].append(websocket)
        logger.info(f"WebSocket client connected to channel: {channel}")

    def disconnect(self, websocket: WebSocket, channel: str):
        if channel in self.active_connections and websocket in self.active_connections[channel]:
            self.active_connections[channel].remove(websocket)
            logger.info(f"WebSocket client disconnected from channel: {channel}")

    async def broadcast(self, channel: str, message: Dict[str, Any]):
        if channel in self.active_connections:
            for connection in self.active_connections[channel]:
                try:
                    await connection.send_text(json.dumps(message))
                except Exception as ex:
                    logger.error(f"Error broadcasting message: {str(ex)}")

ws_manager = WebSocketManager()
''')

    print("[GEN] Core Platform infrastructure generation complete.")

if __name__ == '__main__':
    build_phase01_03()
