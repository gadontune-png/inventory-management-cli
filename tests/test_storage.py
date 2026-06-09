from utils.storage import save_json, load_json

FILE = "data/test.json"


def test_storage():
    data = [{"id": 1}]
    save_json(FILE, data)

    loaded = load_json(FILE)
    assert loaded == data