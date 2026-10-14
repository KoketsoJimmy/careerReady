import json
from pathlib import Path

def load_json(path, default):
    file_path = Path(path)
    try:
        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as f:
                return json.load(f)
    except (OSError, json.JSONDecodeError):
        return default
    return default

def save_json(path, data):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = file_path.with_suffix(file_path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    temp_path.replace(file_path)

def export_json_bytes(data):
    return json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
