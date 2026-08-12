try:
    from distutils.version import StrictVersion
except ImportError:
    from setuptools._distutils.version import StrictVersion

from ops_analytics.suppliers.models import SupplierContract


MIN_CONTRACT_VERSION = "1.0"


def validate_contract_version(version):
    return StrictVersion(version) >= StrictVersion(MIN_CONTRACT_VERSION)


def contract_from_row(row):
    version = row.get("version") or row.get("contract_version") or "1.0"
    if not validate_contract_version(version):
        raise ValueError("Contract version %s is too old" % version)
    return SupplierContract(
        supplier_id=row["supplier_id"],
        version=version,
        rebate_percent=float(row.get("rebate_percent", 0.0)),
        active=str(row.get("active", "true")).lower() != "false",
    )
