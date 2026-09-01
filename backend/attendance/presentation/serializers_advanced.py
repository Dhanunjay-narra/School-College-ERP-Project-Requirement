"""
Smart Attendance Engine — Advanced Exporters, PDF & JSON-LD Serialization.
"""
import json
from typing import List, Dict, Any
from backend.attendance.domain.entities import AttendanceEntity

class AttendanceAdvancedSerializer:
    @staticmethod
    def to_json_ld(entity: AttendanceEntity) -> Dict[str, Any]:
        """Convert aggregate root to W3C JSON-LD format for semantic interoperability."""
        return {
            "@context": "https://schema.org/EducationalOrganization",
            "@type": "Attendance",
            "@id": f"urn:erp:attendance:{entity.id}",
            "identifier": entity.code,
            "name": entity.name,
            "status": entity.status,
            "dateCreated": entity.created_at.isoformat(),
            "dateModified": entity.updated_at.isoformat()
        }

    @staticmethod
    def generate_pdf_summary_spec(entity: AttendanceEntity) -> Dict[str, Any]:
        """Generate ReportLab PDF rendering specification dictionary."""
        return {
            "document_title": f"Official Smart Attendance Engine Record",
            "header": {
                "institution": "Apex Institute of Technology & Management",
                "subsystem": "Smart Attendance Engine",
                "generated_at": entity.updated_at.strftime("%B %d, %Y")
            },
            "sections": [
                {"label": "Record Code", "value": entity.code},
                {"label": "Name / Description", "value": entity.name},
                {"label": "Status", "value": entity.status}
            ]
        }
