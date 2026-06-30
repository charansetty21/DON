from speech.pipeline import SpeechPipeline

pipeline = SpeechPipeline()

text = pipeline.listen()

pipeline.speak(
    f"You said {text}"
)