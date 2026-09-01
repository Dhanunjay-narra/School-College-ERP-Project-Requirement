-- Detailed Finance & General Ledger Table Schema
CREATE TABLE IF NOT EXISTS erp_finance_journal_entries (
    id VARCHAR(36) PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL,
    entry_number VARCHAR(64) UNIQUE NOT NULL,
    entry_date DATE NOT NULL,
    description TEXT NOT NULL,
    total_debit NUMERIC(15,2) NOT NULL,
    total_credit NUMERIC(15,2) NOT NULL,
    status VARCHAR(32) DEFAULT 'POSTED' NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS erp_finance_journal_lines (
    id VARCHAR(36) PRIMARY KEY,
    journal_entry_id VARCHAR(36) REFERENCES erp_finance_journal_entries(id) ON DELETE CASCADE,
    account_code VARCHAR(32) NOT NULL,
    account_name VARCHAR(255) NOT NULL,
    debit NUMERIC(15,2) DEFAULT 0.0 NOT NULL,
    credit NUMERIC(15,2) DEFAULT 0.0 NOT NULL,
    description VARCHAR(255)
);
