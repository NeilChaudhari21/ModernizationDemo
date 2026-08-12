from datetime import datetime


class JobScheduler(object):
    def __init__(self, jobs=[]):
        self.jobs = list(jobs)

    def add(self, name, callback, hour=0):
        self.jobs.append({"name": name, "callback": callback, "hour": hour})

    def run_due(self, current_hour=None):
        current_hour = datetime.utcnow().hour if current_hour is None else current_hour
        results = []
        for job in self.jobs:
            if job["hour"] == current_hour:
                try:
                    results.append(job["callback"]())
                except Exception as exc:
                    results.append({"job": job["name"], "error": str(exc)})
        return results
