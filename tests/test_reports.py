from ops_analytics.inventory.ledger import InventoryLedger
from ops_analytics.reports.inventory_report import build_inventory_report
from ops_analytics.reports.shipment_report import build_shipment_report
from ops_analytics.reports.supplier_report import build_supplier_report


def test_inventory_report_summarizes_ledger():
    ledger = InventoryLedger()
    ledger.receive("SKU-1", 10, 5.0)
    ledger.receive("SKU-2", 30, 2.0)

    report = build_inventory_report(ledger)

    assert report["total_skus"] == 2
    assert report["total_value"] == 110.0
    assert "SKU-1" in report["low_stock"]


def test_supplier_report_from_csv(tmp_path):
    path = tmp_path / "suppliers.csv"
    path.write_text(
        "supplier_id,name,on_time_rate,defect_rate,avg_lead_days,contract_version\n"
        "SUP-1,North Dock,0.96,0.01,5,1.2\n"
    )

    report = build_supplier_report(str(path))

    assert report["count"] == 1
    assert report["rows"][0]["grade"] == "A"


def test_shipment_report_from_csv(tmp_path):
    path = tmp_path / "shipments.csv"
    path.write_text(
        "shipment_id,order_id,status,carrier,origin,destination,shipped_at,delivered_at\n"
        "SHP-1,ORD-1,in_transit,Acme,SEA,PDX,2026-01-01,\n"
    )

    report = build_shipment_report(str(path))

    assert report["total"] == 1
    assert report["in_transit"] == 1
    assert report["rows"][0]["eta_days"] == 1
