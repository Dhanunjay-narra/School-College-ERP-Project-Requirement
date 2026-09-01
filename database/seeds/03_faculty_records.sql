-- Faculty Members and Teaching Assignments
INSERT INTO erp_identity_users (id, tenant_id, email, hashed_password, first_name, last_name, is_active, is_verified, department_id, campus_id) VALUES
('FAC-001', 'default_institution', 'faculty.smith@erp.edu', 'pbkdf2_sha256$demo$hash', 'David', 'Smith', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-002', 'default_institution', 'faculty.iyer@erp.edu', 'pbkdf2_sha256$demo$hash', 'Ananya', 'Iyer', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-003', 'default_institution', 'faculty.jenkins@erp.edu', 'pbkdf2_sha256$demo$hash', 'Sarah', 'Jenkins', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-004', 'default_institution', 'faculty.chang@erp.edu', 'pbkdf2_sha256$demo$hash', 'Michael', 'Chang', TRUE, TRUE, 'CS-DEP', 'MAIN-CAMPUS'),
('FAC-005', 'default_institution', 'faculty.gupta@erp.edu', 'pbkdf2_sha256$demo$hash', 'Amitabh', 'Gupta', TRUE, TRUE, 'MECH-DEP', 'MAIN-CAMPUS');
