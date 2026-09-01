-- Payroll Processing, Salary Structures, and Payslips
CREATE TABLE IF NOT EXISTS erp_payroll_disbursements (
    id VARCHAR(36) PRIMARY KEY,
    employee_id VARCHAR(36) NOT NULL,
    month_year VARCHAR(20) NOT NULL,
    basic_pay NUMERIC(12,2) NOT NULL,
    allowances NUMERIC(12,2) NOT NULL,
    deductions NUMERIC(12,2) NOT NULL,
    net_salary NUMERIC(12,2) NOT NULL,
    disbursement_status VARCHAR(32) DEFAULT 'DISBURSED' NOT NULL
);
