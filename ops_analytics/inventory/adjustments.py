from ops_analytics.audit import write_event


def apply_cycle_count(ledger, sku, counted_quantity, user="system"):
    current = ledger.on_hand(sku)
    delta = int(counted_quantity) - current
    movement = ledger.adjust(sku, delta, reason="cycle_count")
    write_event("inventory.cycle_count", actor=user, details={"sku": sku, "delta": delta})
    return movement


def bulk_adjust(ledger, adjustments, user="system"):
    results = []
    for row in adjustments:
        try:
            results.append(apply_cycle_count(ledger, row["sku"], row["counted_quantity"], user=user))
        except Exception:
            pass
    return results
