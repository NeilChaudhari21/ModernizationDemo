import json
import os
from datetime import datetime

AUDIT_PATH = os.path.join(os.getcwd(), "audit.log")


def build_event(action, actor, details=None):
    details = details or {}
    return {
        "action": action,
        "actor": actor,
        "details": details,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }


def write_event(action, actor="system", details=None, path=AUDIT_PATH):
    event = build_event(action, actor, details)
    line = json.dumps(event, sort_keys=True)
    open(path, "a").write(line + "\n")
    return event


def read_events(path=AUDIT_PATH):
    if not os.path.exists(path):
        return []
    rows = []
    for line in open(path).read().splitlines():
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
    return rows
