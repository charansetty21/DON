import requests
from brain.memory.store import get_memory, add_memory
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
        # 2. Otherwise ask Ollama
        # -----------------------------
        memory = get_memory()
        memory_text = "\n".join(memory[-10:])

        prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{memory_text}

User: {text}
DON:
"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        final_reply = response.json()["response"].strip()

    # -----------------------------
    # 3. Save memory
    # -----------------------------
    add_memory(f"User: {text}")
    add_memory(f"DON: {final_reply}")

    return final_reply