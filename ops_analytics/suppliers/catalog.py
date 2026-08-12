from ops_analytics.csv_utils import read_csv
from ops_analytics.suppliers.scoring import supplier_from_row


def load_supplier_catalog(path):
    rows = read_csv(path, required_fields=["supplier_id", "name"])
    suppliers = []
    for row in rows:
        try:
            suppliers.append(supplier_from_row(row))
        except Exception:
            pass
    return suppliers


def find_supplier(suppliers, supplier_id):
    for supplier in suppliers:
        if supplier.supplier_id == supplier_id:
            return supplier
    return None
