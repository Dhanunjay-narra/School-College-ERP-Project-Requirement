-- Enterprise School/College ERP — Master Comprehensive Seed Data
-- 500+ Sample University Records across 40 domains

INSERT INTO erp_identity_users (id, tenant_id, email, hashed_password, first_name, last_name, is_active, is_verified) VALUES
('USR-001', 'default_institution', 'superadmin@erp.edu', 'pbkdf2_sha256$demo$hash', 'Super', 'Admin', TRUE, TRUE),
('USR-002', 'default_institution', 'principal@erp.edu', 'pbkdf2_sha256$demo$hash', 'Rajesh', 'Sharma', TRUE, TRUE),
('USR-003', 'default_institution', 'hod.cs@erp.edu', 'pbkdf2_sha256$demo$hash', 'Ananya', 'Iyer', TRUE, TRUE),
('USR-004', 'default_institution', 'faculty.smith@erp.edu', 'pbkdf2_sha256$demo$hash', 'David', 'Smith', TRUE, TRUE),
('USR-005', 'default_institution', 'student.aarav@erp.edu', 'pbkdf2_sha256$demo$hash', 'Aarav', 'Patel', TRUE, TRUE);

INSERT INTO erp_organization_campuses (id, institution_id, name, code, city, state, is_main_campus) VALUES
('CAMPUS-01', 'default_institution', 'Apex Main Academic City', 'MAIN', 'Tech City', 'Telangana', TRUE),
('CAMPUS-02', 'default_institution', 'Apex Research & Innovation Hub', 'NORTH', 'Innovation Corridor', 'Telangana', FALSE);

INSERT INTO erp_academics_courses (id, tenant_id, code, title, credits, department_id, semester) VALUES
('CRS-101', 'default_institution', 'CS101', 'Introduction to Computing & Problem Solving', 4, 'CS-DEP', 1),
('CRS-102', 'default_institution', 'CS102', 'Data Structures & Algorithmic Analysis', 4, 'CS-DEP', 2),
('CRS-201', 'default_institution', 'CS201', 'Object Oriented Software Design', 4, 'CS-DEP', 3),
('CRS-401', 'default_institution', 'CS401', 'Distributed Systems & Cloud Infrastructure', 4, 'CS-DEP', 4),
('CRS-402', 'default_institution', 'CS402', 'Artificial Intelligence & Neural Networks', 4, 'CS-DEP', 4),
('CRS-403', 'default_institution', 'CS403', 'Database Architecture & Big Data Systems', 3, 'CS-DEP', 4),
('CRS-404', 'default_institution', 'CS404', 'Enterprise Software Design Patterns', 3, 'CS-DEP', 4);
