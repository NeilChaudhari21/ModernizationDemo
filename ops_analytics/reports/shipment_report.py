from ops_analytics.csv_utils import read_csv
from ops_analytics.reports.templates import report_header
from ops_analytics.shipments.routing import estimate_transit_days
from ops_analytics.shipments.tracking import ShipmentTracker


def build_shipment_report(path):
    rows = read_csv(path)
    tracker = ShipmentTracker().load_rows(rows)
    report_rows = []
    for shipment in tracker.shipments.values():
        report_rows.append({
            "shipment_id": shipment.shipment_id,
            "order_id": shipment.order_id,
            "status": shipment.status,
            "carrier": shipment.carrier,
            "eta_days": estimate_transit_days(shipment.origin, shipment.destination),
        })
    return {
        "header": report_header("Shipment Status"),
        "total": len(report_rows),
        "in_transit": len(tracker.by_status("in_transit")),
        "rows": report_rows,
    }
