-- Document Management & Signatures Production Seed Data
INSERT INTO erp_documents_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('DOCU-001', 'default_institution', 'DOCU-STD-01', 'Primary Active Document Management & Signatures Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('DOCU-002', 'default_institution', 'DOCU-STD-02', 'Secondary Verified Document Management & Signatures Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('DOCU-003', 'default_institution', 'DOCU-STD-03', 'Historical Archived Document Management & Signatures Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
