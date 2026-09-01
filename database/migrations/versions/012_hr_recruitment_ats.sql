-- HR Employee Profiles, Contracts, and Recruitment ATS
CREATE TABLE IF NOT EXISTS erp_hr_employees (
    id VARCHAR(36) PRIMARY KEY,
    employee_code VARCHAR(32) UNIQUE NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    department_id VARCHAR(36) NOT NULL,
    joining_date DATE NOT NULL,
    basic_monthly_salary NUMERIC(12,2) NOT NULL,
    status VARCHAR(32) DEFAULT 'ACTIVE' NOT NULL
);
