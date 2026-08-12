from ops_analytics.config import get_config_value, load_config


def test_config_loading_coerces_basic_values(tmp_path):
    path = tmp_path / "config.ini"
    path.write_text(
        "[app]\n"
        "name = Legacy Ops\n"
        "enabled = true\n"
        "[jobs]\n"
        "daily_hour = 3\n"
    )

    config = load_config(str(path))

    assert config["app"]["name"] == "Legacy Ops"
    assert config["app"]["enabled"] is True
    assert config["jobs"]["daily_hour"] == 3
    assert get_config_value(config, "jobs.daily_hour") == 3
