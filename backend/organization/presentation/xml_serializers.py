"""
Organization & Multi-Campus — Statutory XML & Regulatory Export Serializer.
Formats domain aggregate records into standard institutional XML schemas for organization.
"""
import xml.etree.ElementTree as ET
from typing import List
from backend.organization.domain.entities import OrganizationEntity

class OrganizationXMLSerializer:
    """Generates regulatory XML payloads for Organization & Multi-Campus."""

    @staticmethod
    def to_xml(entities: List[OrganizationEntity]) -> str:
        root = ET.Element("RegulatoryDataset", module="organization", version="1.0")
        for entity in entities:
            elem = ET.SubElement(root, "OrganizationRecord", id=str(entity.id))
            ET.SubElement(elem, "TenantId").text = entity.tenant_id
            ET.SubElement(elem, "Code").text = entity.code
            ET.SubElement(elem, "Name").text = entity.name
            ET.SubElement(elem, "Status").text = entity.status
            ET.SubElement(elem, "CreatedAt").text = entity.created_at.isoformat()
        return ET.tostring(root, encoding="utf-8").decode("utf-8")
