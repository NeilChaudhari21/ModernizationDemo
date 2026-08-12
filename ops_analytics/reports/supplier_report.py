from ops_analytics.csv_utils import read_csv
from ops_analytics.reports.templates import report_header
from ops_analytics.suppliers.catalog import load_supplier_catalog
from ops_analytics.suppliers.scoring import rank_suppliers


def build_supplier_report(path):
    suppliers = load_supplier_catalog(path)
    ranked = rank_suppliers(suppliers)
    return {
        "header": report_header("Supplier Scorecard"),
        "count": len(ranked),
        "rows": ranked,
    }


def build_supplier_csv_preview(path):
    rows = read_csv(path)
    lines = ["supplier_id,name,score,grade"]
    for supplier in rank_suppliers(load_supplier_catalog(path)):
        lines.append("%s,%s,%s,%s" % (supplier["supplier_id"], supplier["name"], supplier["score"], supplier["grade"]))
    return "\n".join(lines)
