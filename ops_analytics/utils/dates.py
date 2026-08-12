from datetime import datetime, timedelta


DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d"]


def now_utc():
    return datetime.utcnow()


def parse_legacy_date(value):
    if not value:
        return None
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except Exception:
            pass
    try:
        return datetime.fromisoformat(value.replace("Z", ""))
    except Exception:
        return None


def days_between(left, right):
    left_dt = parse_legacy_date(left) if isinstance(left, str) else left
    right_dt = parse_legacy_date(right) if isinstance(right, str) else right
    return (right_dt - left_dt).days


def add_business_days(start, days):
    current = start
    added = 0
    while added < days:
        current = current + timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current
