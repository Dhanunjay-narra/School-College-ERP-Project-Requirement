-- Configurable Workflows and Multi-Tier Approvals
CREATE TABLE IF NOT EXISTS erp_workflow_instances (
    id VARCHAR(36) PRIMARY KEY,
    workflow_definition_name VARCHAR(100) NOT NULL,
    initiator_user_id VARCHAR(36) NOT NULL,
    current_tier_number INT DEFAULT 1 NOT NULL,
    approval_status VARCHAR(32) DEFAULT 'PENDING' NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
