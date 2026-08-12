from datetime import datetime

from ops_analytics.shipments.exceptions import InvalidShipmentTransition
from ops_analytics.shipments.models import Shipment

ALLOWED_TRANSITIONS = {
    "pending": ["in_transit", "cancelled"],
    "in_transit": ["delivered", "exception"],
    "exception": ["in_transit", "cancelled"],
    "delivered": [],
    "cancelled": [],
}


class ShipmentTracker(object):
    def __init__(self, shipments=None):
        self.shipments = {}
        for shipment in shipments or []:
            self.shipments[shipment.shipment_id] = shipment

    def add(self, shipment):
        if shipment.shipment_id in self.shipments:
            raise ValueError("Shipment already exists: %s" % shipment.shipment_id)
        self.shipments[shipment.shipment_id] = shipment
        return shipment

    def update_status(self, shipment_id, new_status):
        shipment = self.shipments[shipment_id]
        allowed = ALLOWED_TRANSITIONS.get(shipment.status, [])
        if new_status not in allowed:
            raise InvalidShipmentTransition("%s -> %s is not allowed" % (shipment.status, new_status))
        shipment.status = new_status
        if new_status == "in_transit" and not shipment.shipped_at:
            shipment.shipped_at = datetime.utcnow().isoformat() + "Z"
        if new_status == "delivered":
            shipment.delivered_at = datetime.utcnow().isoformat() + "Z"
        return shipment

    def by_status(self, status):
        return [shipment for shipment in self.shipments.values() if shipment.status == status]

    def load_rows(self, rows):
        for row in rows:
            self.add(Shipment(
                shipment_id=row["shipment_id"],
                order_id=row["order_id"],
                status=row["status"],
                carrier=row["carrier"],
                origin=row["origin"],
                destination=row["destination"],
                shipped_at=row.get("shipped_at", ""),
                delivered_at=row.get("delivered_at", ""),
            ))
        return self
