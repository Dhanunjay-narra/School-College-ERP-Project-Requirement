-- Transportation Fleet, Routes, and Real-Time Telemetry
CREATE TABLE IF NOT EXISTS erp_transport_fleet (
    id VARCHAR(36) PRIMARY KEY,
    vehicle_number VARCHAR(32) UNIQUE NOT NULL,
    vehicle_type VARCHAR(32) DEFAULT 'BUS' NOT NULL,
    seating_capacity INT NOT NULL,
    driver_user_id VARCHAR(36) NOT NULL,
    insurance_valid_until DATE NOT NULL,
    fitness_valid_until DATE NOT NULL
);
