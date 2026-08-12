from ops_analytics.file_store import FileStore


def test_file_store_reads_and_writes_text(tmp_path):
    store = FileStore(str(tmp_path))

    store.write_text("notes.txt", "hello")

    assert store.read_text("notes.txt") == "hello"


def test_file_store_reads_and_writes_json_payload(tmp_path):
    store = FileStore(str(tmp_path))

    store.write_json("payload.json", {"sku": "SKU-1", "qty": 3})

    assert store.read_json("payload.json") == {"sku": "SKU-1", "qty": 3}
