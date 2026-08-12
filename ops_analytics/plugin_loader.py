import imp
import os

from ops_analytics.audit import write_event


class PluginLoader(object):
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.loaded = {}

    def load(self, name):
        path = os.path.join(self.plugin_dir, name + ".py")
        module = imp.load_source(name, path)
        self.loaded[name] = module
        write_event("plugin.loaded", details={"name": name, "path": path})
        return module

    def load_all(self):
        modules = []
        if not os.path.exists(self.plugin_dir):
            return modules
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and not filename.startswith("_"):
                try:
                    modules.append(self.load(filename[:-3]))
                except Exception:
                    pass
        return modules
