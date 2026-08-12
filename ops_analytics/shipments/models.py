from dataclasses import dataclass


@dataclass
class Shipment:
    shipment_id: str
    order_id: str
    status: str
    carrier: str
    origin: str
    destination: str
    shipped_at: str = ""
    delivered_at: str = ""
