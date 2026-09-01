-- Admissions CRM & Merit Engine Production Seed Data
INSERT INTO erp_admissions_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ADMI-001', 'default_institution', 'ADMI-STD-01', 'Primary Active Admissions CRM & Merit Engine Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ADMI-002', 'default_institution', 'ADMI-STD-02', 'Secondary Verified Admissions CRM & Merit Engine Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ADMI-003', 'default_institution', 'ADMI-STD-03', 'Historical Archived Admissions CRM & Merit Engine Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
