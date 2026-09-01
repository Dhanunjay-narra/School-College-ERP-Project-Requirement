-- Hostel Residential Life, Rooms, and Mess Services
CREATE TABLE IF NOT EXISTS erp_hostels_buildings (
    id VARCHAR(36) PRIMARY KEY,
    building_name VARCHAR(255) NOT NULL,
    gender_type VARCHAR(20) NOT NULL,
    total_rooms INT NOT NULL,
    warden_user_id VARCHAR(36) NOT NULL
);
