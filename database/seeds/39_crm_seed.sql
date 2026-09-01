-- Institutional CRM & Admissions Leads Production Seed Data
INSERT INTO erp_crm_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('CRM-001', 'default_institution', 'CRM-STD-01', 'Primary Active Institutional CRM & Admissions Leads Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('CRM-002', 'default_institution', 'CRM-STD-02', 'Secondary Verified Institutional CRM & Admissions Leads Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('CRM-003', 'default_institution', 'CRM-STD-03', 'Historical Archived Institutional CRM & Admissions Leads Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
