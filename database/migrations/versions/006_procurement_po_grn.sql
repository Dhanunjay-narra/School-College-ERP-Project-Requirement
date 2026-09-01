-- Procurement, Purchase Orders & Goods Receipt Notes
CREATE TABLE IF NOT EXISTS erp_procurement_orders (
    id VARCHAR(36) PRIMARY KEY,
    po_number VARCHAR(64) UNIQUE NOT NULL,
    vendor_id VARCHAR(36) NOT NULL,
    total_amount NUMERIC(15,2) NOT NULL,
    status VARCHAR(32) DEFAULT 'DRAFT' NOT NULL,
    delivery_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS erp_procurement_grn (
    id VARCHAR(36) PRIMARY KEY,
    grn_number VARCHAR(64) UNIQUE NOT NULL,
    po_id VARCHAR(36) REFERENCES erp_procurement_orders(id),
    received_by VARCHAR(36) NOT NULL,
    inspection_passed BOOLEAN DEFAULT TRUE NOT NULL,
    received_date DATE NOT NULL
);
