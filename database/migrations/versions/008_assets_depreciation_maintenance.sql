-- Asset Lifecycle, QR Tagging, and Maintenance Tickets
CREATE TABLE IF NOT EXISTS erp_assets_registry (
    id VARCHAR(36) PRIMARY KEY,
    asset_tag VARCHAR(64) UNIQUE NOT NULL,
    asset_name VARCHAR(255) NOT NULL,
    category VARCHAR(64) NOT NULL,
    purchase_cost NUMERIC(12,2) NOT NULL,
    current_book_value NUMERIC(12,2) NOT NULL,
    depreciation_rate_annual NUMERIC(5,2) DEFAULT 10.0 NOT NULL,
    location_room_id VARCHAR(36) NOT NULL,
    assigned_user_id VARCHAR(36)
);
