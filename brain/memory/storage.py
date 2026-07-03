import json
import os

MEMORY_FILE = "brain/memory/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_memory(role: str, content: str):
    memory = load_memory()

    memory.append(
        {
            "role": role,
            "content": content
        }
    )

    save_memory(memory)


def get_memory():
    return load_memory()


def clear_memory():
    save_memory([])