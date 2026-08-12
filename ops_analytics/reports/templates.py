from datetime import datetime


def report_header(title):
    return {
        "title": title,
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }


def as_text_table(rows, columns):
    lines = [" | ".join(columns)]
    lines.append("-" * len(lines[0]))
    for row in rows:
        values = []
        for col in columns:
            values.append(str(row.get(col, "")))
        lines.append(" | ".join(values))
    return "\n".join(lines)
