import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from ops_analytics.config import load_config
from ops_analytics.jobs.daily_jobs import run_daily_reports


if __name__ == "__main__":
    config = load_config(os.path.join(ROOT, "examples", "config.ini"))
    run_daily_reports(config)
