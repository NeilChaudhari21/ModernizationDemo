import argparse
import json
import os

from tabulate import tabulate

from ops_analytics.csv_utils import read_csv
from ops_analytics.inventory.ledger import InventoryLedger
from ops_analytics.reports.inventory_report import build_inventory_report
from ops_analytics.reports.shipment_report import build_shipment_report
from ops_analytics.reports.supplier_report import build_supplier_report


def _print_json(data):
    print(json.dumps(data, indent=2, sort_keys=True))


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ops-analytics")
    sub = parser.add_subparsers(dest="command")

    inv = sub.add_parser("inventory-report")
    inv.add_argument("path")

    sup = sub.add_parser("supplier-report")
    sup.add_argument("path")

    shp = sub.add_parser("shipment-report")
    shp.add_argument("path")

    args = parser.parse_args(argv)

    if args.command == "inventory-report":
        rows = read_csv(args.path)
        ledger = InventoryLedger()
        for row in rows:
            ledger.receive(row["sku"], int(row["on_hand"]), float(row["unit_cost"]))
        _print_json(build_inventory_report(ledger))
    elif args.command == "supplier-report":
        _print_json(build_supplier_report(args.path))
    elif args.command == "shipment-report":
        _print_json(build_shipment_report(args.path))
    else:
        parser.print_help()


def print_table(rows):
    if not rows:
        print("No rows")
        return
    print(tabulate(rows, headers="keys"))


def locate_example(name):
    return os.path.join(os.getcwd(), "examples", name)


if __name__ == "__main__":
    main()
