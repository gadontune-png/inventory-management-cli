import json
import os

STATE_FILE = "data/state.json"


def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "supplier_id": 0,
            "product_id": 0,
            "warehouse_id": 0,
            "transaction_id": 0
        }
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)