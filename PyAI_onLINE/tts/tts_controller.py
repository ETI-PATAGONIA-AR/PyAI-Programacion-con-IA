from .tts_engine import TTSEngine
from .text_filter import extract_speakable_text


class TTSController:
    def __init__(self):
        self.tts = TTSEngine()

    def speak_ai_response(self, full_text: str):
        speakable_text = extract_speakable_text(full_text)
        self.tts.speak(speakable_text)
