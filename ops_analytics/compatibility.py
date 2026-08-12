import os
import pkgutil
import platform


try:
    from collections import Mapping
except ImportError:
    from collections.abc import Mapping


def is_mapping(value):
    return isinstance(value, Mapping)


def find_optional_loader(module_name):
    return pkgutil.find_loader(module_name)


def get_platform_name():
    try:
        dist = platform.dist()
        if dist and dist[0]:
            return "%s-%s" % (dist[0], dist[1])
    except Exception:
        pass
    return platform.platform()


def legacy_home_dir():
    return os.environ.get("OPS_HOME") or os.path.expanduser("~/.ops_analytics")
