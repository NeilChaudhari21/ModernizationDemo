# Legacy Ops Analytics

Legacy Ops Analytics is a fictional internal warehouse and logistics analytics
platform. It models inventory movements, supplier performance, shipment
tracking, order pricing, simple forecasting, CSV/JSON reports, and batch jobs.

This repository is intentionally written as a larger legacy-style Python 3.14
codebase. It still runs on Python 3.14, but it contains realistic migration and
modernization issues that would need assessment before moving to Python 3.14.

## Requirements

- Python 3.14
- pytest
- packaging
- python-dateutil
- tabulate
- PyYAML

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## CLI Usage

Generate an inventory report from sample data:

```bash
python -m ops_analytics.cli inventory-report examples/inventory.csv
```

Generate a shipment report:

```bash
python -m ops_analytics.cli shipment-report examples/shipments.csv
```

Score suppliers:

```bash
python -m ops_analytics.cli supplier-report examples/suppliers.csv
```

## Testing

Run the test suite:

```bash
python -m pytest
```

The tox configuration includes Python 3.14:

```bash
tox
```

## Sample Data

The `examples/` directory includes CSV and INI files for inventory, orders,
suppliers, shipments, and application configuration.

## Migration Notes

This project intentionally keeps old idioms such as `distutils`,
`imp.load_source`, `pkgutil.find_loader`, `SafeConfigParser`, `datetime.utcnow`,
legacy `collections.Mapping` imports, broad exception handling, and ad hoc file
I/O. These are part of the migration assessment surface and should not be
modernized in this baseline repository.
