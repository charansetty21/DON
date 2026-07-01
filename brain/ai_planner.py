import requests

from brain.registry import list_tool_descriptions

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"


def choose_tool(user_input):

    tools = list_tool_descriptions()

    prompt = f"""
You are DON's Planner.

Available tools:

{tools}

Choose ONLY ONE tool.

Return ONLY the tool name.

If no tool matches return:

chat

User:

{user_input}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=60,
    )

    return response.json()["response"].strip()