-- Document Management & Signatures Extended Seed Entries
INSERT INTO erp_documents_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('DOCU-EXT-01', 'default_institution', 'DOCU-EXT-1', 'Extended Document Management & Signatures Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('DOCU-EXT-02', 'default_institution', 'DOCU-EXT-2', 'Extended Document Management & Signatures Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
