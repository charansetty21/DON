import subprocess


class AudioPlayer:

    def play(self, path: str):
        subprocess.run(["afplay", path])