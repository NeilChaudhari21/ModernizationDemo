import os
from datetime import datetime, timedelta


def cleanup_old_reports(path, older_than_days=90, dry_run=True):
    cutoff = datetime.utcnow() - timedelta(days=older_than_days)
    removed = []
    if not os.path.exists(path):
        return removed
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        try:
            mtime = datetime.utcfromtimestamp(os.path.getmtime(full_path))
            if mtime < cutoff:
                removed.append(full_path)
                if not dry_run:
                    os.remove(full_path)
        except Exception:
            continue
    return removed
