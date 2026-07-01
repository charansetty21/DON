import requests

from brain.memory import get_memory, add_memory
from brain.tools.router import run_tool

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"

SYSTEM_PROMPT = """
You are DON, an intelligent AI assistant.

Always call the user "Boss".

Be helpful, concise, and professional.
"""


def chat(text: str) -> str:
    # -----------------------------
    # 1. Check if a tool can handle it
    # -----------------------------
    tool_result = run_tool(text)

    if tool_result is not None:
        final_reply = f"Boss, {tool_result}"

    else:
        # -----------------------------
        # 2. Load conversation memory
        # -----------------------------
        memory = get_memory()

        memory_text = "\n".join(
            f"{msg['role'].capitalize()}: {msg['content']}"
            for msg in memory[-10:]
        )

        # -----------------------------
        # 3. Build prompt
        # -----------------------------
        prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{memory_text}

User: {text}
DON:
"""

        # -----------------------------
        # 4. Ask Ollama
        # -----------------------------
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        final_reply = response.json()["response"].strip()

    # -----------------------------
    # 5. Save conversation
    # -----------------------------
    add_memory("user", text)
    add_memory("assistant", final_reply)

    return final_reply