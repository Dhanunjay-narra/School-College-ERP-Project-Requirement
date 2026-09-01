"""
Campus Inventory & Multi-Store Warehouse API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/inventory", tags=["Campus Inventory & Stores"])

class InventoryItem(BaseModel):
    sku: str
    item_name: str
    category: str
    store_location: str
    current_quantity: int
    reorder_level: int
    unit: str
    status: str

@router.get("/stock", response_model=List[InventoryItem])
async def list_inventory_stock():
    return [
        InventoryItem(sku="SKU-CS-LAB-01", item_name="Dell OptiPlex Core i7 Workstation", category="Computers & Hardware", store_location="Computer Store (ACB-002)", current_quantity=65, reorder_level=10, unit="Units", status="IN_STOCK"),
        InventoryItem(sku="SKU-CHE-LAB-12", item_name="Sodium Hydroxide Analytical Grade 500g", category="Laboratory Consumables", store_location="Science Store (SC-101)", current_quantity=24, reorder_level=5, unit="Bottles", status="IN_STOCK"),
        InventoryItem(sku="SKU-STAT-004", item_name="A4 Examination Answer Booklets (32-Page)", category="Stationery & Printing", store_location="Central Store (ADM-010)", current_quantity=12000, reorder_level=2000, unit="Booklets", status="IN_STOCK"),
    ]
