-- AI/ML Predictive Intelligence Extended Seed Entries
INSERT INTO erp_ai_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('AI-EXT-01', 'default_institution', 'AI-EXT-1', 'Extended AI/ML Predictive Intelligence Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('AI-EXT-02', 'default_institution', 'AI-EXT-2', 'Extended AI/ML Predictive Intelligence Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
