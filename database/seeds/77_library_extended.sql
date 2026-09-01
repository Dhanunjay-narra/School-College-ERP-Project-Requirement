-- Library & RFID Circulation Extended Seed Entries
INSERT INTO erp_library_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('LIBR-EXT-01', 'default_institution', 'LIBR-EXT-1', 'Extended Library & RFID Circulation Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('LIBR-EXT-02', 'default_institution', 'LIBR-EXT-2', 'Extended Library & RFID Circulation Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
