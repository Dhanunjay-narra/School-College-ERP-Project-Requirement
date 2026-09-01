"""
Applicant Tracking System — Anti-Corruption Layer (ACL) Translator.
Translates external entity representations to Applicant Tracking System aggregate roots.
"""
from typing import Dict, Any, Optional
from backend.recruitment.domain.entities import RecruitmentEntity

class RecruitmentACLTranslator:
    """Isolates Applicant Tracking System domain from external legacy formats."""

    @classmethod
    def translate_from_external_source(cls, external_data: Dict[str, Any], tenant_id: str = "default_institution") -> RecruitmentEntity:
        return RecruitmentEntity(
            id=str(external_data.get("external_id") or external_data.get("id", "")),
            tenant_id=tenant_id,
            code=str(external_data.get("legacy_code") or external_data.get("code", "EXT")),
            name=str(external_data.get("display_name") or external_data.get("name", "External Entry")),
            status=str(external_data.get("state") or external_data.get("status", "ACTIVE")),
            metadata=dict(external_data.get("extra_attributes") or {})
        )
