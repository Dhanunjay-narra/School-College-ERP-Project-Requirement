-- Institutional CRM & Admissions Leads Extended Seed Entries
INSERT INTO erp_crm_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('CRM-EXT-01', 'default_institution', 'CRM-EXT-1', 'Extended Institutional CRM & Admissions Leads Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('CRM-EXT-02', 'default_institution', 'CRM-EXT-2', 'Extended Institutional CRM & Admissions Leads Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
