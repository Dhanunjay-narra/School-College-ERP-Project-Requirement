-- Library Catalog, MARC21, and RFID Circulation
CREATE TABLE IF NOT EXISTS erp_library_catalog (
    id VARCHAR(36) PRIMARY KEY,
    isbn VARCHAR(32) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    authors VARCHAR(255) NOT NULL,
    total_copies INT DEFAULT 1 NOT NULL,
    available_copies INT DEFAULT 1 NOT NULL,
    shelf_location VARCHAR(64) NOT NULL
);
