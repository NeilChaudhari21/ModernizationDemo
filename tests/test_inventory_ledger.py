import pytest

from ops_analytics.inventory.ledger import InventoryLedger


def test_inventory_ledger_receives_and_ships_stock():
    ledger = InventoryLedger()
    ledger.receive("SKU-1", 10, 2.0)
    ledger.receive("SKU-1", 5, 4.0)
    ledger.ship("SKU-1", 3)

    assert ledger.on_hand("SKU-1") == 12
    assert ledger.average_cost("SKU-1") == 2.6667
    assert ledger.inventory_value("SKU-1") == 32.0


def test_inventory_ledger_blocks_overshipment():
    ledger = InventoryLedger()
    ledger.receive("SKU-1", 2, 1.0)

    with pytest.raises(ValueError):
        ledger.ship("SKU-1", 3)
