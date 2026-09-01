-- Campus Events & Conferences Production Seed Data
INSERT INTO erp_events_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('EVEN-001', 'default_institution', 'EVEN-STD-01', 'Primary Active Campus Events & Conferences Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('EVEN-002', 'default_institution', 'EVEN-STD-02', 'Secondary Verified Campus Events & Conferences Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('EVEN-003', 'default_institution', 'EVEN-STD-03', 'Historical Archived Campus Events & Conferences Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
