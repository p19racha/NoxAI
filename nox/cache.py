import json
import os

CACHE_FILE = "nox_cache.json"
MAX_ENTRIES = 10

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return []
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_to_cache(prompt, response):
    cache = load_cache()
    cache.append({"prompt": prompt, "response": response})
    cache = cache[-MAX_ENTRIES:]  # keep last 10
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

def get_last_cache():
    return load_cache()
