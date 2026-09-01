CREATE TABLE IF NOT EXISTS erp_identity_users (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL DEFAULT 'default_institution',
                email VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                phone_number VARCHAR(30),
                is_active BOOLEAN DEFAULT TRUE NOT NULL,
                is_verified BOOLEAN DEFAULT FALSE NOT NULL,
                mfa_enabled BOOLEAN DEFAULT FALSE NOT NULL,
                mfa_secret VARCHAR(64),
                department_id VARCHAR(64),
                campus_id VARCHAR(64),
                failed_login_attempts INT DEFAULT 0 NOT NULL,
                locked_until TIMESTAMP WITH TIME ZONE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
                is_deleted BOOLEAN DEFAULT FALSE NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_users_email ON erp_identity_users(email);
            CREATE INDEX IF NOT EXISTS idx_users_tenant ON erp_identity_users(tenant_id);
