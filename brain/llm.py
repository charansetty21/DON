import time
import requests

from brain.memory import get_memory, add_memory
from brain.tools.router import run_tool

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"

SYSTEM_PROMPT = """
You are DON, an intelligent AI assistant.

Always call the user "Boss".

Be helpful, concise, and professional.
"""


def chat(text: str) -> str:
    # --------------------------------------------------
    # 1. Check whether a tool can handle the request
    # --------------------------------------------------
    tool_result = run_tool(text)

    if tool_result is not None:
        final_reply = f"Boss, {tool_result}"

    else:
        # --------------------------------------------------
        # 2. Load conversation history
        # --------------------------------------------------
        messages = get_memory()

        # Only keep the latest 20 messages
        messages = messages[-20:]

        chat_messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        chat_messages.extend(messages)

        chat_messages.append(
            {
                "role": "user",
                "content": text
            }
        )

        print(f"[LLM] Sending {len(chat_messages)} messages to Ollama...")

        # --------------------------------------------------
        # 3. Send request to Ollama
        # --------------------------------------------------
        start = time.time()

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": chat_messages,
                "stream": False
            },
        )

        elapsed = time.time() - start
        print(f"[LLM] Ollama response time: {elapsed:.2f} sec")

        if response.status_code != 200:
            print("\n========== OLLAMA ERROR ==========")
            print("Status:", response.status_code)
            print("Response:", response.text)
            print("==================================\n")
            return "Boss, Ollama returned an error."

        data = response.json()
        final_reply = data["message"]["content"].strip()

    # --------------------------------------------------
    # 4. Save conversation
    # --------------------------------------------------
    add_memory("user", text)
    add_memory("assistant", final_reply)

    return final_reply