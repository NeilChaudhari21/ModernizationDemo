from dataclasses import dataclass


@dataclass
class Supplier:
    supplier_id: str
    name: str
    on_time_rate: float
    defect_rate: float
    avg_lead_days: int
    contract_version: str = "1.0"


@dataclass
class SupplierContract:
    supplier_id: str
    version: str
    rebate_percent: float
    active: bool = True
