from ops_analytics.versioning import choose_latest, compare_versions, is_supported_runtime


def test_compare_versions_uses_legacy_loose_version_semantics():
    assert compare_versions("1.0", "1.0.1") == -1
    assert compare_versions("2.0", "1.9") == 1
    assert compare_versions("1.0", "1.0") == 0


def test_choose_latest_version():
    assert choose_latest(["1.0", "1.0.5", "0.9"]) == "1.0.5"


def test_supported_runtime_floor():
    assert is_supported_runtime("3.10")
