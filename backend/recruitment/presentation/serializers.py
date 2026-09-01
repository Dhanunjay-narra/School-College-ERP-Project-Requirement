"""
Applicant Tracking System — Serializers, Formatter & Exporters.
Provides CSV, JSON, and XML serialization routines for recruitment.
"""
import json
import csv
import io
from typing import List, Dict, Any
from backend.recruitment.domain.entities import RecruitmentEntity

class RecruitmentSerializer:
    @staticmethod
    def to_json(entity: RecruitmentEntity) -> str:
        return json.dumps(entity.to_dict(), indent=2)

    @staticmethod
    def to_csv(entities: List[RecruitmentEntity]) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "Tenant ID", "Code", "Name", "Status", "Created At"])
        for e in entities:
            writer.writerow([e.id, e.tenant_id, e.code, e.name, e.status, e.created_at.isoformat()])
        return output.getvalue()

    @staticmethod
    def to_summary(entity: RecruitmentEntity) -> Dict[str, Any]:
        return {
            "id": entity.id,
            "title": f"{entity.code} — {entity.name}",
            "status": entity.status,
            "created_at": entity.created_at.strftime("%Y-%m-%d %H:%M")
        }
