"""
Universal Enterprise Reporting — Statutory XML & Regulatory Export Serializer.
Formats domain aggregate records into standard institutional XML schemas for reporting.
"""
import xml.etree.ElementTree as ET
from typing import List
from backend.reporting.domain.entities import ReportingEntity

class ReportingXMLSerializer:
    """Generates regulatory XML payloads for Universal Enterprise Reporting."""

    @staticmethod
    def to_xml(entities: List[ReportingEntity]) -> str:
        root = ET.Element("RegulatoryDataset", module="reporting", version="1.0")
        for entity in entities:
            elem = ET.SubElement(root, "ReportingRecord", id=str(entity.id))
            ET.SubElement(elem, "TenantId").text = entity.tenant_id
            ET.SubElement(elem, "Code").text = entity.code
            ET.SubElement(elem, "Name").text = entity.name
            ET.SubElement(elem, "Status").text = entity.status
            ET.SubElement(elem, "CreatedAt").text = entity.created_at.isoformat()
        return ET.tostring(root, encoding="utf-8").decode("utf-8")
