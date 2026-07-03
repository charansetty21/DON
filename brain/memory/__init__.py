import time
import requests

from brain.memory import memory
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
    # 1. Check if a tool can handle the request
    # --------------------------------------------------
    tool_result = run_tool(text)

    if tool_result is not None:
        final_reply = f"Boss, {tool_result}"

    else:
        # --------------------------------------------------
        # 2. Get conversation history from RAM
        # --------------------------------------------------
        messages = memory.get_messages()

        chat_messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        chat_messages.extend(messages)

        chat_messages.append(
            {
                "role": "user",
                "content": text,
            }
        )

        print(f"[LLM] Sending {len(chat_messages)} messages...")

        # --------------------------------------------------
        # 3. Call Ollama Chat API
        # --------------------------------------------------
        start = time.time()

        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "messages": chat_messages,
                    "stream": False,
                },
                timeout=120,
            )

            elapsed = time.time() - start
            print(f"[LLM] Response time: {elapsed:.2f} sec")

            if response.status_code != 200:
                print("\n========== OLLAMA ERROR ==========")
                print("Status:", response.status_code)
                print("Response:", response.text)
                print("==================================\n")
                return "Boss, Ollama returned an error."

            data = response.json()

            final_reply = data["message"]["content"].strip()

        except requests.exceptions.RequestException as e:
            print(f"[LLM ERROR] {e}")
            return "Boss, I couldn't connect to Ollama."

    # --------------------------------------------------
    # 4. Save conversation in RAM and Disk
    # --------------------------------------------------
    memory.add_user_message(text)
    memory.add_assistant_message(final_reply)

    return final_reply