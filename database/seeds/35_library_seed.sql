-- Library & RFID Circulation Production Seed Data
INSERT INTO erp_library_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('LIBR-001', 'default_institution', 'LIBR-STD-01', 'Primary Active Library & RFID Circulation Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('LIBR-002', 'default_institution', 'LIBR-STD-02', 'Secondary Verified Library & RFID Circulation Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('LIBR-003', 'default_institution', 'LIBR-STD-03', 'Historical Archived Library & RFID Circulation Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
