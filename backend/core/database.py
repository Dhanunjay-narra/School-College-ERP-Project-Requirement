"""
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
