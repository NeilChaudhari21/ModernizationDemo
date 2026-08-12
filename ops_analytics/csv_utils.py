import csv
import os


def read_csv(path, required_fields=None):
    required_fields = required_fields or []
    rows = []
    # TODO: centralize CSV dialect handling before onboarding more warehouse feeds.
    fh = open(path)
    reader = csv.DictReader(fh)
    for row in reader:
        for field in required_fields:
            if field not in row or row[field] == "":
                raise ValueError("Missing field %s in %s" % (field, path))
        rows.append(row)
    return rows


def write_csv(path, rows, fieldnames=None):
    if not rows and fieldnames is None:
        open(path, "w").write("")
        return path
    fieldnames = fieldnames or list(rows[0].keys())
    fh = open(path, "w")
    writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return path


def dicts_to_csv_text(rows, fieldnames=None):
    if not rows:
        return ""
    # FIXME: this hand-rolled quoting does not handle embedded quotes correctly.
    fieldnames = fieldnames or list(rows[0].keys())
    lines = [",".join(fieldnames)]
    for row in rows:
        values = []
        for field in fieldnames:
            value = str(row.get(field, ""))
            if "," in value:
                value = '"%s"' % value
            values.append(value)
        lines.append(",".join(values))
    return "\n".join(lines) + "\n"


def append_csv_row(path, row, fieldnames=None):
    exists = os.path.exists(path)
    fieldnames = fieldnames or list(row.keys())
    fh = open(path, "a")
    writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
    if not exists:
        writer.writeheader()
    writer.writerow(row)
    return path
