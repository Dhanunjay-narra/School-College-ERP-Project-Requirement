-- Academic Structure, Campuses, and Departments Seed Data
INSERT INTO erp_organization_institutions (id, tenant_id, name, code, institution_type, accreditation, affiliation, currency, timezone, contact_email, contact_phone, address)
VALUES ('default_institution', 'default_institution', 'Apex Institute of Technology & Management', 'AITM', 'UNIVERSITY', 'NAAC A++ Grade, NBA Accredited, ISO 9001:2015', 'Apex Technical University', 'INR', 'Asia/Kolkata', 'contact@erp.edu', '+91-11-23456789', 'Institutional Area, Knowledge Park, Tech City')
ON CONFLICT (code) DO NOTHING;

INSERT INTO erp_organization_campuses (id, institution_id, name, code, city, state, is_main_campus)
VALUES 
('CAMPUS-01', 'default_institution', 'Main Academic Campus', 'MAIN', 'Tech City', 'Telangana', TRUE),
('CAMPUS-02', 'default_institution', 'North Research & Innovation Hub', 'NORTH', 'Innovation Corridor', 'Telangana', FALSE),
('CAMPUS-03', 'default_institution', 'South Medical & Life Sciences Campus', 'SOUTH', 'Health Valley', 'Telangana', FALSE)
ON CONFLICT (id) DO NOTHING;
