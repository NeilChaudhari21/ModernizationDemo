from distutils.core import setup

setup(
    name="legacy-ops-analytics",
    version="0.9.4",
    packages=[
        "ops_analytics",
        "ops_analytics.inventory",
        "ops_analytics.suppliers",
        "ops_analytics.orders",
        "ops_analytics.shipments",
        "ops_analytics.reports",
        "ops_analytics.jobs",
        "ops_analytics.utils",
    ],
    python_requires=">=3.10",
)
