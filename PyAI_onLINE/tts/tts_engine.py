import pyttsx3


SABINA_VOICE_ID = (
    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\"
    "TTS_MS_ES-MX_SABINA_11.0"
)


class TTSEngine:
    def __init__(self, rate=175, volume=1.0):
        self.engine = pyttsx3.init("sapi5")
        self.engine.setProperty("voice", SABINA_VOICE_ID)
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

    def speak(self, text: str):
        if not text.strip():
            return
        self.engine.say(text)
        self.engine.runAndWait()
