import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from ops_analytics.shipments.tracking import ShipmentTracker


def main():
    tracker = ShipmentTracker()
    sample_file = os.path.join(ROOT, "examples", "shipments.csv")
    print("Loaded tracker for %s" % sample_file)
    return tracker


if __name__ == "__main__":
    main()
