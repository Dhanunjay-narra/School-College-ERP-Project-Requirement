CREATE TABLE IF NOT EXISTS erp_organization_institutions (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                name VARCHAR(255) NOT NULL,
                code VARCHAR(50) UNIQUE NOT NULL,
                institution_type VARCHAR(50) NOT NULL,
                accreditation VARCHAR(255),
                affiliation VARCHAR(255),
                currency VARCHAR(10) DEFAULT 'INR',
                timezone VARCHAR(50) DEFAULT 'Asia/Kolkata',
                contact_email VARCHAR(255),
                contact_phone VARCHAR(50),
                address TEXT,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
