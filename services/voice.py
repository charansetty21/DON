from pathlib import Path
import subprocess
import shutil


class VoiceService:
    """
    DON Voice Service
    Handles text-to-speech using Piper.
    """

    def __init__(self):
        self.model_path = None

        # Find the piper executable automatically
        self.piper = shutil.which("piper")

        if self.piper is None:
            raise FileNotFoundError(
                "Piper executable not found. Is your virtual environment activated?"
            )

    def load_voice(self, model_path: str):
        model = Path(model_path)

        if not model.exists():
            raise FileNotFoundError(f"Voice model not found: {model}")

        self.model_path = model

    def speak(self, text: str):
        if self.model_path is None:
            raise RuntimeError("No voice model loaded.")

        output_dir = Path("assets/voices/output")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "don.wav"

        command = [
            self.piper,
            "--model",
            str(self.model_path),
            "--output_file",
            str(output_file),
        ]

        result = subprocess.run(
            command,
            input=text,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        subprocess.run(["afplay", str(output_file)], check=True)