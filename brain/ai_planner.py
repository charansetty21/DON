import json
import requests

from brain.tools.tool_registry import list_tools

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"


SYSTEM_PROMPT = """
You are DON's planning engine.

Your job is to decide whether the user needs a tool.

Available actions:

1. tool
2. chat

Return ONLY valid JSON.

Example:

{
    "action":"tool",
    "tool":"current_time",
    "arguments":{}
}

Example:

{
    "action":"chat"
}
"""


def build_prompt(user_input: str):

    tools = json.dumps(
        list_tools(),
        indent=2,
    )

    return f"""
{SYSTEM_PROMPT}

Available Tools:

{tools}

User Request:

{user_input}

JSON:
"""


def plan(user_input: str):

    prompt = build_prompt(user_input)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
    )

    response.raise_for_status()

    text = response.json()["response"].strip()

    return text