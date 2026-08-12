try:
    from distutils.version import LooseVersion
except ImportError:
    from setuptools._distutils.version import LooseVersion

APP_VERSION = "0.9.4"


def compare_versions(left, right):
    left_v = LooseVersion(str(left))
    right_v = LooseVersion(str(right))
    if left_v < right_v:
        return -1
    if left_v > right_v:
        return 1
    return 0


def is_supported_runtime(version_text):
    return compare_versions(version_text, "3.10") >= 0


def choose_latest(versions):
    latest = None
    for version in versions:
        if latest is None or compare_versions(version, latest) > 0:
            latest = version
    return latest
