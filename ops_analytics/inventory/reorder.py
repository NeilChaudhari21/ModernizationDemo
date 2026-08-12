REORDER_BUFFER = 5


def reorder_recommendations(items, recent_sales=None):
    recent_sales = recent_sales or {}
    recommendations = []
    for item in items:
        sales_velocity = int(recent_sales.get(item.sku, 0))
        target = item.reorder_point + sales_velocity + REORDER_BUFFER
        if item.on_hand < target:
            recommendations.append({
                "sku": item.sku,
                "recommended_qty": target - item.on_hand,
                "reason": "on hand %s below target %s" % (item.on_hand, target),
            })
    return recommendations
