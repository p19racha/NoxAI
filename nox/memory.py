import json
import os

MEMORY_FILE = "nox_memory.json"

def _load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def _save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def store_memory(key, value):
    memory = _load_memory()
    memory[key.lower()] = value
    _save_memory(memory)
    print(f"💾 Remembered: {key} = {value}")

def get_memory(key):
    memory = _load_memory()
    return memory.get(key.lower())
