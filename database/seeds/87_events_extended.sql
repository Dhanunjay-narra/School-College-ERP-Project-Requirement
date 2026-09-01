-- Campus Events & Conferences Extended Seed Entries
INSERT INTO erp_events_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('EVEN-EXT-01', 'default_institution', 'EVEN-EXT-1', 'Extended Campus Events & Conferences Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('EVEN-EXT-02', 'default_institution', 'EVEN-EXT-2', 'Extended Campus Events & Conferences Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
