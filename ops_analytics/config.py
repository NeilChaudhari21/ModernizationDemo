import configparser
import os

import yaml

DEFAULT_CONFIG_PATH = os.path.join(os.getcwd(), "examples", "config.ini")


def _new_parser():
    try:
        return configparser.SafeConfigParser()
    except AttributeError:
        return configparser.ConfigParser()


def load_config(path=DEFAULT_CONFIG_PATH):
    parser = _new_parser()
    parser.read(path)
    data = {}
    for section in parser.sections():
        data[section] = {}
        for key, value in parser.items(section):
            data[section][key] = _coerce_value(value)
    return data


def load_yaml_config(path):
    try:
        text = open(path).read()
        return yaml.safe_load(text) or {}
    except Exception:
        return {}


def _coerce_value(value):
    if value is None:
        return value
    lower = value.lower()
    if lower in ("true", "yes", "on"):
        return True
    if lower in ("false", "no", "off"):
        return False
    try:
        return int(value)
    except Exception:
        pass
    try:
        return float(value)
    except Exception:
        return value


def get_config_value(config, dotted_name, default=None):
    section, key = dotted_name.split(".", 1)
    try:
        return config[section][key]
    except Exception:
        return default
