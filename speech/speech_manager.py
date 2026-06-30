from config import VOICE_OUTPUT
from speech.audio import AudioPlayer
from speech.xtts_engine import XTTSEngine


class SpeechManager:

    def __init__(self):
        self.engine = XTTSEngine()
        self.player = AudioPlayer()

    def speak(self, text: str):
        self.engine.speak(text)
        self.player.play(VOICE_OUTPUT)