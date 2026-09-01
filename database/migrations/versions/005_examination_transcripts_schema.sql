-- Examinations, Moderation, Grade Points & Transcripts
CREATE TABLE IF NOT EXISTS erp_examinations_grades (
    id VARCHAR(36) PRIMARY KEY,
    student_id VARCHAR(36) NOT NULL,
    course_id VARCHAR(64) NOT NULL,
    semester INT NOT NULL,
    internal_marks NUMERIC(5,2) NOT NULL,
    end_sem_marks NUMERIC(5,2) NOT NULL,
    total_marks NUMERIC(5,2) NOT NULL,
    letter_grade VARCHAR(5) NOT NULL,
    grade_point NUMERIC(4,2) NOT NULL,
    result_status VARCHAR(20) DEFAULT 'PASS' NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
