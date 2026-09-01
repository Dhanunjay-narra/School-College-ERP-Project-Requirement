"""
Campus Store & Cafeteria POS — Advanced Exporters, PDF & JSON-LD Serialization.
"""
import json
from typing import List, Dict, Any
from backend.campus_store.domain.entities import CampusStoreEntity

class CampusStoreAdvancedSerializer:
    @staticmethod
    def to_json_ld(entity: CampusStoreEntity) -> Dict[str, Any]:
        """Convert aggregate root to W3C JSON-LD format for semantic interoperability."""
        return {
            "@context": "https://schema.org/EducationalOrganization",
            "@type": "CampusStore",
            "@id": f"urn:erp:campus_store:{entity.id}",
            "identifier": entity.code,
            "name": entity.name,
            "status": entity.status,
            "dateCreated": entity.created_at.isoformat(),
            "dateModified": entity.updated_at.isoformat()
        }

    @staticmethod
    def generate_pdf_summary_spec(entity: CampusStoreEntity) -> Dict[str, Any]:
        """Generate ReportLab PDF rendering specification dictionary."""
        return {
            "document_title": f"Official Campus Store & Cafeteria POS Record",
            "header": {
                "institution": "Apex Institute of Technology & Management",
                "subsystem": "Campus Store & Cafeteria POS",
                "generated_at": entity.updated_at.strftime("%B %d, %Y")
            },
            "sections": [
                {"label": "Record Code", "value": entity.code},
                {"label": "Name / Description", "value": entity.name},
                {"label": "Status", "value": entity.status}
            ]
        }
