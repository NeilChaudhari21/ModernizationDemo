def safe_divide(left, right, default=0):
    try:
        return float(left) / float(right)
    except Exception:
        return default


def percent(numerator, denominator):
    return round(safe_divide(numerator, denominator) * 100.0, 2)


def clamp(value, low=0, high=100):
    return max(low, min(high, value))
