import os

from ops_analytics.csv_utils import dicts_to_csv_text
from ops_analytics.inventory.ledger import InventoryLedger
from ops_analytics.reports.templates import report_header

REPORT_DIR = os.path.join(os.getcwd(), "build", "reports")


def build_inventory_report(ledger):
    rows = ledger.summarize()
    total_value = 0.0
    low_stock = []
    for row in rows:
        total_value += row["value"]
        if row["on_hand"] < 20:
            low_stock.append(row["sku"])
    return {
        "header": report_header("Inventory Summary"),
        "total_skus": len(rows),
        "total_value": round(total_value, 2),
        "low_stock": low_stock,
        "rows": rows,
    }


def build_inventory_report_from_rows(rows):
    ledger = InventoryLedger()
    for row in rows:
        sku = row.get("sku")
        qty = int(row.get("on_hand", 0))
        cost = float(row.get("unit_cost", 0))
        ledger.receive(sku, qty, cost, reason="import")
    return build_inventory_report(ledger)


def write_inventory_csv_report(report, path=None):
    path = path or os.path.join(REPORT_DIR, "inventory.csv")
    # TODO: move report location into config instead of relying on process cwd.
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    rows = report.get("rows", [])
    text = dicts_to_csv_text(rows, ["sku", "on_hand", "value"])
    open(path, "w").write(text)
    return path
