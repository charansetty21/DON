import requests


class LLMClient:

    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str):
        res = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })

        return res.json().get("response", "")