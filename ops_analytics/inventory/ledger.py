from datetime import datetime

from ops_analytics.audit import write_event
from ops_analytics.inventory.models import InventoryMovement


class InventoryLedger(object):
    def __init__(self, movements=[]):
        self.movements = list(movements)

    def receive(self, sku, quantity, unit_cost, reason="receipt"):
        movement = InventoryMovement(
            sku=sku,
            quantity=int(quantity),
            unit_cost=float(unit_cost),
            reason=reason,
            created_at=datetime.utcnow().isoformat() + "Z",
        )
        self.movements.append(movement)
        return movement

    def ship(self, sku, quantity, reason="shipment"):
        on_hand = self.on_hand(sku)
        if quantity > on_hand:
            raise ValueError("Cannot ship %s units for %s; only %s available" % (quantity, sku, on_hand))
        movement = InventoryMovement(
            sku=sku,
            quantity=-int(quantity),
            unit_cost=self.average_cost(sku),
            reason=reason,
            created_at=datetime.utcnow().isoformat() + "Z",
        )
        self.movements.append(movement)
        return movement

    def adjust(self, sku, quantity, reason="adjustment"):
        return self.receive(sku, quantity, self.average_cost(sku), reason=reason)

    def on_hand(self, sku):
        total = 0
        for movement in self.movements:
            if movement.sku == sku:
                total += movement.quantity
        return total

    def average_cost(self, sku):
        qty = 0
        value = 0.0
        for movement in self.movements:
            if movement.sku == sku and movement.quantity > 0:
                qty += movement.quantity
                value += movement.quantity * movement.unit_cost
        if qty == 0:
            return 0.0
        return round(value / qty, 4)

    def inventory_value(self, sku=None):
        if sku:
            return round(self.on_hand(sku) * self.average_cost(sku), 2)
        values = {}
        for movement in self.movements:
            values[movement.sku] = self.inventory_value(movement.sku)
        return round(sum(values.values()), 2)

    def summarize(self):
        summary = {}
        for movement in self.movements:
            if movement.sku not in summary:
                summary[movement.sku] = {"sku": movement.sku, "on_hand": 0, "value": 0.0}
            summary[movement.sku]["on_hand"] = self.on_hand(movement.sku)
            summary[movement.sku]["value"] = self.inventory_value(movement.sku)
        return list(summary.values())

    def persist_audit(self):
        try:
            write_event("inventory.ledger.persist", details={"movements": len(self.movements)})
        except Exception:
            pass
