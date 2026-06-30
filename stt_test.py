from speech.stt import SpeechToText

stt = SpeechToText()

text = stt.transcribe("assets/output/input.wav")

print("\nRecognized Text:")
print(text)