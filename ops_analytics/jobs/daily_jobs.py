import os

from ops_analytics.csv_utils import read_csv
from ops_analytics.reports.inventory_report import build_inventory_report_from_rows, write_inventory_csv_report
from ops_analytics.reports.shipment_report import build_shipment_report
from ops_analytics.reports.supplier_report import build_supplier_report


def run_daily_reports(config):
    data_dir = config.get("app", {}).get("data_dir", "./examples")
    output_dir = config.get("reports", {}).get("output_dir", "./build/reports")
    inventory_rows = read_csv(os.path.join(data_dir, "inventory.csv"))
    inventory = build_inventory_report_from_rows(inventory_rows)
    write_inventory_csv_report(inventory, os.path.join(output_dir, "inventory.csv"))
    supplier = build_supplier_report(os.path.join(data_dir, "suppliers.csv"))
    shipment = build_shipment_report(os.path.join(data_dir, "shipments.csv"))
    return {"inventory": inventory, "supplier": supplier, "shipment": shipment}
