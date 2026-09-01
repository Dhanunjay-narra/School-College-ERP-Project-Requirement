"""
Faculty & Workload Management — Advanced Exporters, PDF & JSON-LD Serialization.
"""
import json
from typing import List, Dict, Any
from backend.faculty.domain.entities import FacultyEntity

class FacultyAdvancedSerializer:
    @staticmethod
    def to_json_ld(entity: FacultyEntity) -> Dict[str, Any]:
        """Convert aggregate root to W3C JSON-LD format for semantic interoperability."""
        return {
            "@context": "https://schema.org/EducationalOrganization",
            "@type": "Faculty",
            "@id": f"urn:erp:faculty:{entity.id}",
            "identifier": entity.code,
            "name": entity.name,
            "status": entity.status,
            "dateCreated": entity.created_at.isoformat(),
            "dateModified": entity.updated_at.isoformat()
        }

    @staticmethod
    def generate_pdf_summary_spec(entity: FacultyEntity) -> Dict[str, Any]:
        """Generate ReportLab PDF rendering specification dictionary."""
        return {
            "document_title": f"Official Faculty & Workload Management Record",
            "header": {
                "institution": "Apex Institute of Technology & Management",
                "subsystem": "Faculty & Workload Management",
                "generated_at": entity.updated_at.strftime("%B %d, %Y")
            },
            "sections": [
                {"label": "Record Code", "value": entity.code},
                {"label": "Name / Description", "value": entity.name},
                {"label": "Status", "value": entity.status}
            ]
        }
