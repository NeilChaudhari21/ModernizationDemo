import os
import platform
import subprocess


def get_env_flag(name, default=False):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.lower() in ("1", "true", "yes", "on")


def describe_runtime():
    try:
        dist = platform.dist()
    except Exception:
        dist = ("unknown", "", "")
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "dist": dist,
        "home": os.path.expanduser("~"),
    }


def legacy_shell_echo(message):
    command = "echo %s" % message
    return subprocess.check_output(command, shell=True).decode("utf-8").strip()
