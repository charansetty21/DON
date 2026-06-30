from services.voice import VoiceService

voice = VoiceService()

voice.load_voice(
    "assets/voices/models/en_US-lessac-medium.onnx"
)

voice.speak(
    "Good morning Boss. I am DON. System initialization complete."
)