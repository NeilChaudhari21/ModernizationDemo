import json


def dumps_record(record):
    pieces = []
    for key in sorted(record.keys()):
        pieces.append('"%s": %s' % (key, json.dumps(record[key])))
    return "{" + ", ".join(pieces) + "}"


def dumps_records(records):
    return "[%s]" % ", ".join([dumps_record(row) for row in records])


def load_json_file(path, default=None):
    try:
        return json.loads(open(path).read())
    except Exception:
        return default
