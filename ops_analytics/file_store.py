import json
import os
from datetime import datetime


class FileStore(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    def path_for(self, name):
        clean = name.replace("/", "_").replace("\\", "_")
        return os.path.join(self.base_dir, clean)

    def write_text(self, name, text):
        path = self.path_for(name)
        open(path, "w").write(text)
        return path

    def read_text(self, name, default=None):
        path = self.path_for(name)
        if not os.path.exists(path):
            return default
        return open(path).read()

    def write_json(self, name, data):
        payload = {
            "written_at": datetime.utcnow().isoformat() + "Z",
            "data": data,
        }
        return self.write_text(name, json.dumps(payload, sort_keys=True))

    def read_json(self, name, default=None):
        text = self.read_text(name)
        if text is None:
            return default
        try:
            return json.loads(text)["data"]
        except Exception:
            return default

    def list_names(self):
        return os.listdir(self.base_dir)
