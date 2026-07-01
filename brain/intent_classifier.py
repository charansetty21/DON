import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"


def classify_intent(user_input: str):

    prompt = f"""
You are DON's Intent Classifier.

Your job is to classify the user's request.

Return ONLY one of these labels.

chat
web_search
open_app
create_file
read_file
write_file
delete_file
rename_file
create_folder
add_note
show_notes
clear_notes
time
date
list_files
current_directory

User:
{user_input}

Answer:
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

    intent = response.json()["response"].strip().lower()

    return intent