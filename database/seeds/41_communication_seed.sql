-- Universal Multi-Channel Notifications Production Seed Data
INSERT INTO erp_communication_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('COMM-001', 'default_institution', 'COMM-STD-01', 'Primary Active Universal Multi-Channel Notifications Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('COMM-002', 'default_institution', 'COMM-STD-02', 'Secondary Verified Universal Multi-Channel Notifications Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('COMM-003', 'default_institution', 'COMM-STD-03', 'Historical Archived Universal Multi-Channel Notifications Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
