from speech.recorder import Recorder
from speech.stt import SpeechToText
from speech.speech_manager import SpeechManager


class SpeechPipeline:

    def __init__(self):
        print("Initializing Speech Pipeline...")

        self.recorder = Recorder()
        self.stt = SpeechToText()
        self.speech = SpeechManager()

        print("Speech Pipeline Ready.")

    def listen(self):

        audio_file = self.recorder.record()

        text = self.stt.transcribe(audio_file)

        print(f"\nBoss said: {text}")

        return text

    def speak(self, text):

        self.speech.speak(text)