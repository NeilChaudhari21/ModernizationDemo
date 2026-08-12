from dataclasses import dataclass


@dataclass
class InventoryItem:
    sku: str
    name: str
    on_hand: int
    unit_cost: float
    location: str = "UNKNOWN"
    reorder_point: int = 0

    def value(self):
        return self.on_hand * self.unit_cost


@dataclass
class InventoryMovement:
    sku: str
    quantity: int
    unit_cost: float
    reason: str
    created_at: str
