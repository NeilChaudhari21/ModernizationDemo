from ops_analytics.suppliers.models import Supplier
from ops_analytics.suppliers.scoring import grade_supplier, rank_suppliers, score_supplier


def test_supplier_scoring_balances_quality_delivery_and_lead_time():
    supplier = Supplier("SUP-1", "North Dock", 0.95, 0.02, 4, "1.2")

    assert score_supplier(supplier) == 94.4
    assert grade_supplier(score_supplier(supplier)) == "A"


def test_supplier_ranking_orders_by_score():
    suppliers = [
        Supplier("SUP-2", "Slow Co", 0.7, 0.08, 12, "1.0"),
        Supplier("SUP-1", "Fast Co", 0.96, 0.01, 5, "1.2"),
    ]

    ranked = rank_suppliers(suppliers)

    assert ranked[0]["supplier_id"] == "SUP-1"
    assert ranked[0]["grade"] == "A"
