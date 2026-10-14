import json
from modules.storage import load_json, save_json

def test_save_and_load_json(tmp_path):
    path = tmp_path / "sample.json"
    save_json(str(path), {"name": "CareerReady"})
    assert load_json(str(path), {}) == {"name": "CareerReady"}

def test_missing_file_returns_default(tmp_path):
    assert load_json(str(tmp_path / "missing.json"), []) == []
