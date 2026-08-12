from ops_analytics.suppliers.models import Supplier


def supplier_from_row(row):
    return Supplier(
        supplier_id=row["supplier_id"],
        name=row["name"],
        on_time_rate=float(row["on_time_rate"]),
        defect_rate=float(row["defect_rate"]),
        avg_lead_days=int(row["avg_lead_days"]),
        contract_version=row.get("contract_version", "1.0"),
    )


def score_supplier(supplier, weights={"on_time": 60, "quality": 30, "lead": 10}):
    on_time = supplier.on_time_rate * weights["on_time"]
    quality = (1.0 - supplier.defect_rate) * weights["quality"]
    lead_penalty = min(supplier.avg_lead_days, 20) / 20.0
    lead = (1.0 - lead_penalty) * weights["lead"]
    score = on_time + quality + lead
    return round(score, 2)


def grade_supplier(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "D"


def rank_suppliers(suppliers):
    rows = []
    for supplier in suppliers:
        score = score_supplier(supplier)
        rows.append({"supplier_id": supplier.supplier_id, "name": supplier.name, "score": score, "grade": grade_supplier(score)})
    return sorted(rows, key=lambda row: row["score"], reverse=True)
