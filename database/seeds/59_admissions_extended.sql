-- Admissions CRM & Merit Engine Extended Seed Entries
INSERT INTO erp_admissions_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ADMI-EXT-01', 'default_institution', 'ADMI-EXT-1', 'Extended Admissions CRM & Merit Engine Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ADMI-EXT-02', 'default_institution', 'ADMI-EXT-2', 'Extended Admissions CRM & Merit Engine Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
