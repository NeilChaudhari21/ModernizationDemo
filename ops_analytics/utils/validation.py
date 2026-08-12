def require_fields(row, fields):
    missing = []
    for field in fields:
        if field not in row or row[field] in ("", None):
            missing.append(field)
    if missing:
        raise ValueError("Missing fields: %s" % ", ".join(missing))
    return True


def coerce_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default


def coerce_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default
