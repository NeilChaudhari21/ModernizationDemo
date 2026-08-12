DISCOUNTS = {
    "standard": 0.0,
    "gold": 0.05,
    "enterprise": 0.12,
}


def discount_for_tier(tier):
    return DISCOUNTS.get((tier or "standard").lower(), 0.0)


def bulk_discount(quantity):
    if quantity >= 100:
        return 0.08
    if quantity >= 50:
        return 0.04
    if quantity >= 20:
        return 0.02
    return 0.0
