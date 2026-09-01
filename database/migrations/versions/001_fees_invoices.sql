CREATE TABLE IF NOT EXISTS erp_fees_invoices (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                invoice_number VARCHAR(64) UNIQUE NOT NULL,
                student_id VARCHAR(36) REFERENCES erp_students_records(id),
                description VARCHAR(255) NOT NULL,
                amount_due NUMERIC(12, 2) NOT NULL,
                amount_paid NUMERIC(12, 2) DEFAULT 0.0 NOT NULL,
                balance NUMERIC(12, 2) NOT NULL,
                due_date DATE NOT NULL,
                status VARCHAR(32) DEFAULT 'PENDING' NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
