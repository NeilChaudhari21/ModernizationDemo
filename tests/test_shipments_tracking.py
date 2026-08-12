import pytest

from ops_analytics.shipments.exceptions import InvalidShipmentTransition
from ops_analytics.shipments.models import Shipment
from ops_analytics.shipments.tracking import ShipmentTracker


def test_shipment_tracker_allows_valid_status_flow():
    tracker = ShipmentTracker()
    tracker.add(Shipment("SHP-1", "ORD-1", "pending", "Acme", "SEA", "PDX"))

    tracker.update_status("SHP-1", "in_transit")
    shipment = tracker.update_status("SHP-1", "delivered")

    assert shipment.status == "delivered"
    assert shipment.shipped_at
    assert shipment.delivered_at


def test_shipment_tracker_rejects_invalid_transition():
    tracker = ShipmentTracker([Shipment("SHP-1", "ORD-1", "pending", "Acme", "SEA", "PDX")])

    with pytest.raises(InvalidShipmentTransition):
        tracker.update_status("SHP-1", "delivered")
