-- Smart Biometric & Gate Attendance Logs
CREATE TABLE IF NOT EXISTS erp_attendance_sessions (
    id VARCHAR(36) PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL,
    course_id VARCHAR(64) NOT NULL,
    faculty_id VARCHAR(64) NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room_number VARCHAR(32) NOT NULL,
    total_enrolled INT NOT NULL,
    total_present INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
