import whisper
import pyttsx3
import sounddevice as sd
import numpy as np
import tempfile
from scipy.io.wavfile import write

# TTS engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Try to force male voice (Apple Alex preferred)
selected_voice = None

for v in voices:
    if "alex" in v.name.lower():
        selected_voice = v.id
        break

# fallback if Alex not found
if selected_voice is None:
    selected_voice = voices[0].id

engine.setProperty('voice', selected_voice)
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)


def speak(text: str):
    print("DON:", text)
    engine.say(text)
    engine.runAndWait()


# load whisper model (small = fast)
model = whisper.load_model("base")

def listen():
    print("🎤 Listening... Speak now Boss (8 sec window)")

    duration = 8
    fs = 16000

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()

    recording = np.squeeze(recording)

    print("🧠 Processing...")

    result = model.transcribe(
        recording,
        fp16=False,
        language="en"
    )

    text = result["text"].strip()

    print("You:", text)
    return text
