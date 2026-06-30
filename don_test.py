from TTS.api import TTS

from config import (
    VOICE_MODEL,
    VOICE_REFERENCE,
    VOICE_LANGUAGE,
    VOICE_OUTPUT,
)

print("Loading XTTS...")

tts = TTS(VOICE_MODEL)

print("Generating speech...")

tts.tts_to_file(
    text="Hello Boss. I am DON. Your assistant is now active.",
    speaker_wav=VOICE_REFERENCE,
    language=VOICE_LANGUAGE,
    file_path=VOICE_OUTPUT,
)

print("Done!")