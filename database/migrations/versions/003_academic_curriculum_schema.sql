-- Detailed Curriculum, Prerequisites & Elective Offerings
CREATE TABLE IF NOT EXISTS erp_academics_curriculum (
    id VARCHAR(36) PRIMARY KEY,
    program_id VARCHAR(64) NOT NULL,
    semester INT NOT NULL,
    course_id VARCHAR(64) NOT NULL,
    is_mandatory BOOLEAN DEFAULT TRUE NOT NULL,
    min_pass_grade VARCHAR(5) DEFAULT 'C' NOT NULL
);

CREATE TABLE IF NOT EXISTS erp_academics_prerequisites (
    id VARCHAR(36) PRIMARY KEY,
    course_id VARCHAR(64) NOT NULL,
    required_prerequisite_course_id VARCHAR(64) NOT NULL,
    min_required_grade VARCHAR(5) DEFAULT 'C' NOT NULL
);
