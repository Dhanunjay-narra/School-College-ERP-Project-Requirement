"""
Campus Store & Cafeteria POS — Serializers, Formatter & Exporters.
Provides CSV, JSON, and XML serialization routines for campus_store.
"""
import json
import csv
import io
from typing import List, Dict, Any
from backend.campus_store.domain.entities import CampusStoreEntity

class CampusStoreSerializer:
    @staticmethod
    def to_json(entity: CampusStoreEntity) -> str:
        return json.dumps(entity.to_dict(), indent=2)

    @staticmethod
    def to_csv(entities: List[CampusStoreEntity]) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "Tenant ID", "Code", "Name", "Status", "Created At"])
        for e in entities:
            writer.writerow([e.id, e.tenant_id, e.code, e.name, e.status, e.created_at.isoformat()])
        return output.getvalue()

    @staticmethod
    def to_summary(entity: CampusStoreEntity) -> Dict[str, Any]:
        return {
            "id": entity.id,
            "title": f"{entity.code} — {entity.name}",
            "status": entity.status,
            "created_at": entity.created_at.strftime("%Y-%m-%d %H:%M")
        }
