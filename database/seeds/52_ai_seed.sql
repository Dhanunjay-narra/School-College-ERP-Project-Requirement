-- AI/ML Predictive Intelligence Production Seed Data
INSERT INTO erp_ai_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('AI-001', 'default_institution', 'AI-STD-01', 'Primary Active AI/ML Predictive Intelligence Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('AI-002', 'default_institution', 'AI-STD-02', 'Secondary Verified AI/ML Predictive Intelligence Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('AI-003', 'default_institution', 'AI-STD-03', 'Historical Archived AI/ML Predictive Intelligence Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
