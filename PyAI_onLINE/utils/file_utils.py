#==================================================================
# PyAI_v1\utils\file_utils.py - ETI Patagonia
#==================================================================
import json

def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
