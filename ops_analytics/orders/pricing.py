from ops_analytics.orders.discounts import bulk_discount, discount_for_tier

TAX_RATE = 0.0875
FUEL_SURCHARGE = 3.5


def calculate_order_total(order, include_tax=True, fees=[]):
    subtotal = 0.0
    total_qty = 0
    for line in order.lines:
        subtotal += float(line.quantity) * float(line.unit_price)
        total_qty += int(line.quantity)

    discount_rate = discount_for_tier(order.customer_tier) + bulk_discount(total_qty)
    discount = round(subtotal * discount_rate, 2)
    fees_total = sum([float(fee) for fee in fees])
    taxable = subtotal - discount + fees_total + FUEL_SURCHARGE
    tax = round(taxable * TAX_RATE, 2) if include_tax else 0.0
    return {
        "order_id": order.order_id,
        "subtotal": round(subtotal, 2),
        "discount": discount,
        "fees": round(fees_total + FUEL_SURCHARGE, 2),
        "tax": tax,
        "total": round(taxable + tax, 2),
    }


def price_lines_from_csv_rows(rows):
    priced = []
    for row in rows:
        try:
            qty = int(row["quantity"])
            unit = float(row["unit_price"])
            total = qty * unit
            priced.append({"sku": row["sku"], "quantity": qty, "line_total": "%.2f" % total})
        except:
            continue
    return priced
