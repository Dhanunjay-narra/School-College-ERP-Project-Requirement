"""
Accounts Payable & Receivable — Anti-Corruption Layer (ACL) Translator.
Translates external entity representations to Accounts Payable & Receivable aggregate roots.
"""
from typing import Dict, Any, Optional
from backend.accounting.domain.entities import AccountingEntity

class AccountingACLTranslator:
    """Isolates Accounts Payable & Receivable domain from external legacy formats."""

    @classmethod
    def translate_from_external_source(cls, external_data: Dict[str, Any], tenant_id: str = "default_institution") -> AccountingEntity:
        return AccountingEntity(
            id=str(external_data.get("external_id") or external_data.get("id", "")),
            tenant_id=tenant_id,
            code=str(external_data.get("legacy_code") or external_data.get("code", "EXT")),
            name=str(external_data.get("display_name") or external_data.get("name", "External Entry")),
            status=str(external_data.get("state") or external_data.get("status", "ACTIVE")),
            metadata=dict(external_data.get("extra_attributes") or {})
        )
