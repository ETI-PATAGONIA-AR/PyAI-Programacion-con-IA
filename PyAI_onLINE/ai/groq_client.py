#==================================================================
# PyAI_v1\ai\groq_client.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================
import requests
from utils.file_utils import read_text, read_json

class GroqClient:
    API_URL = "https://api.groq.com/openai/v1/chat/completions"

    def __init__(self):
        self.api_key = read_text("config/api_key.txt").strip()
        self.settings = read_json("config/settings.json")
        self.system_prompt = read_text("config/system_prompt.txt")

    def ask(self, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.settings["model"],
            "temperature": self.settings["temperature"],
            "max_tokens": self.settings["max_tokens"],
            "messages": messages
        }

        r = requests.post(self.API_URL, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
