from dataclasses import dataclass


@dataclass
class OrderLine:
    sku: str
    quantity: int
    unit_price: float

    def subtotal(self):
        return self.quantity * self.unit_price


@dataclass
class Order:
    order_id: str
    customer_tier: str
    lines: list
    ordered_at: str = ""
