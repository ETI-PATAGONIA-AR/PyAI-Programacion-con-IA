#==================================================================
# PyAI_v1\core\history_store.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================

import json
import os

PATH = "data/conversations.json"

def load_history():
    if not os.path.exists(PATH):
        return []
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_history(history):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
