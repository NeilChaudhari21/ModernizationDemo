from datetime import datetime

from dateutil.parser import parse


def moving_average(values, window=3):
    if not values:
        return 0
    window_values = values[-window:]
    return sum(window_values) / float(len(window_values))


def forecast_orders(rows, sku):
    quantities = []
    for row in rows:
        if row.get("sku") == sku:
            try:
                parse(row.get("ordered_at"))
                quantities.append(int(row.get("quantity", 0)))
            except Exception:
                pass
    forecast = moving_average(quantities)
    return {
        "sku": sku,
        "forecast_quantity": round(forecast, 2),
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }
