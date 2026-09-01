-- Accreditation & Regulatory Compliance Extended Seed Entries
INSERT INTO erp_compliance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('COMP-EXT-01', 'default_institution', 'COMP-EXT-1', 'Extended Accreditation & Regulatory Compliance Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('COMP-EXT-02', 'default_institution', 'COMP-EXT-2', 'Extended Accreditation & Regulatory Compliance Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
