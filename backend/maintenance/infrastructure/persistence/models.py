"""
Campus Facility Maintenance — SQLAlchemy ORM Persistence Models.
"""
from sqlalchemy import Column, String, DateTime, Text, JSON, Boolean, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from backend.core.database import BaseEntity

class MaintenanceORM(BaseEntity):
    __tablename__ = "erp_maintenance_records"

    code: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="ACTIVE", nullable=False, index=True)
    details_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
