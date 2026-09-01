-- Multi-Store Warehouses and Item SKUs
CREATE TABLE IF NOT EXISTS erp_inventory_warehouses (
    id VARCHAR(36) PRIMARY KEY,
    code VARCHAR(32) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    campus_id VARCHAR(36) NOT NULL,
    manager_id VARCHAR(36)
);

CREATE TABLE IF NOT EXISTS erp_inventory_items (
    id VARCHAR(36) PRIMARY KEY,
    sku VARCHAR(64) UNIQUE NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    warehouse_id VARCHAR(36) REFERENCES erp_inventory_warehouses(id),
    quantity_on_hand INT DEFAULT 0 NOT NULL,
    reorder_level INT DEFAULT 10 NOT NULL,
    unit_of_measure VARCHAR(32) DEFAULT 'Units' NOT NULL
);
