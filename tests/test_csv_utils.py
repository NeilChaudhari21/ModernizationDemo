import pytest

from ops_analytics.csv_utils import dicts_to_csv_text, read_csv, write_csv


def test_read_csv_validates_required_fields(tmp_path):
    path = tmp_path / "inventory.csv"
    path.write_text("sku,on_hand\nSKU-1,3\n")

    rows = read_csv(str(path), required_fields=["sku", "on_hand"])

    assert rows == [{"sku": "SKU-1", "on_hand": "3"}]


def test_read_csv_raises_for_missing_required_field(tmp_path):
    path = tmp_path / "inventory.csv"
    path.write_text("sku,on_hand\nSKU-1,\n")

    with pytest.raises(ValueError):
        read_csv(str(path), required_fields=["sku", "on_hand"])


def test_dicts_to_csv_text_repeats_legacy_formatting():
    text = dicts_to_csv_text([{"sku": "SKU-1", "name": "Widget, A"}], ["sku", "name"])

    assert text == 'sku,name\nSKU-1,"Widget, A"\n'
