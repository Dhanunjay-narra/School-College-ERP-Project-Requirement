-- Institutional CRM, Alumni Network, and Endowments
CREATE TABLE IF NOT EXISTS erp_alumni_records (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    graduation_year INT NOT NULL,
    current_company VARCHAR(255),
    designation VARCHAR(100),
    total_donations_contributed NUMERIC(12,2) DEFAULT 0.0
);
