def fifo_value(movements):
    remaining = {}
    for movement in movements:
        rows = remaining.setdefault(movement.sku, [])
        if movement.quantity > 0:
            rows.append([movement.quantity, movement.unit_cost])
        else:
            qty = abs(movement.quantity)
            while qty and rows:
                head = rows[0]
                used = min(qty, head[0])
                head[0] -= used
                qty -= used
                if head[0] == 0:
                    rows.pop(0)
    total = 0.0
    for sku in remaining:
        for qty, cost in remaining[sku]:
            total += qty * cost
    return round(total, 2)


def weighted_average_value(ledger):
    return ledger.inventory_value()
