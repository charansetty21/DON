import json
import re
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"

SYSTEM_PROMPT = """
You are DON's planning engine.

Your ONLY job is to decide whether the user's request needs:

1. chat
2. tool

Rules:

- Greetings -> chat
- General questions -> chat
- Requests to open apps -> tool
- File operations -> tool
- Notes -> tool
- Web searches -> tool
- System commands -> tool

Reply ONLY with JSON.

Examples:

User: Hello
{"action":"chat"}

User: Open Chrome
{"action":"tool"}

User: What time is it?
{"action":"tool"}
"""


def clean_json(text: str) -> str:
    """
    Remove markdown code fences if the model returns them.
    """
    text = text.strip()

    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    return text.strip()


def plan(user_input: str):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": messages,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        reply = response.json()["message"]["content"]

        reply = clean_json(reply)

        return json.loads(reply)

    except Exception as e:
        print("[AI Planner Error]", e)

        return {
            "action": "chat"
        }