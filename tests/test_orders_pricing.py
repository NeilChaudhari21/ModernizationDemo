from ops_analytics.orders.models import Order, OrderLine
from ops_analytics.orders.pricing import calculate_order_total


def test_order_pricing_applies_tier_discount_tax_and_fuel_fee():
    order = Order(
        order_id="ORD-1",
        customer_tier="gold",
        lines=[OrderLine("SKU-1", 10, 10.0)],
    )

    priced = calculate_order_total(order)

    assert priced["subtotal"] == 100.0
    assert priced["discount"] == 5.0
    assert priced["fees"] == 3.5
    assert priced["tax"] == 8.62
    assert priced["total"] == 107.12
