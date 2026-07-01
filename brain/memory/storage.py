import json
import os

MEMORY_FILE = "brain/memory/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)


def add_memory(role: str, content: str):
    messages = load_memory()

    messages.append({
        "role": role,
        "content": content
    })

    save_memory(messages)


def get_memory():
    return load_memory()


def clear_memory():
    save_memory([])