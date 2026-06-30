from TTS.api import TTS

from config import (
    VOICE_MODEL,
    VOICE_REFERENCE,
    VOICE_LANGUAGE,
    VOICE_OUTPUT,
)

from speech.tts import TTSEngine


class XTTSEngine(TTSEngine):

    def __init__(self):
        print("Loading XTTS...")
        self.tts = TTS(VOICE_MODEL)
        print("XTTS Ready.")

    def speak(self, text: str):
        self.tts.tts_to_file(
            text=text,
            speaker_wav=VOICE_REFERENCE,
            language=VOICE_LANGUAGE,
            file_path=VOICE_OUTPUT,
        )