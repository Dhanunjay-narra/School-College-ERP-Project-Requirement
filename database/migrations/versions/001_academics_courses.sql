CREATE TABLE IF NOT EXISTS erp_academics_courses (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                code VARCHAR(32) NOT NULL,
                title VARCHAR(255) NOT NULL,
                credits INT DEFAULT 3 NOT NULL,
                department_id VARCHAR(64) NOT NULL,
                semester INT NOT NULL,
                syllabus_url TEXT,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
