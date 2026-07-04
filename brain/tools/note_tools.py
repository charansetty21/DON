import json
import os

from brain.tools.tool_registry import register

NOTES_FILE = "data/notes.json"


def _ensure_notes_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            json.dump([], f)


def _load_notes():
    _ensure_notes_file()

    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def _save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)


def create_note(text):
    notes = _load_notes()

def create_note(text):
    notes = _load_notes()

    # prevent duplicate exact notes
    if any(n["text"] == text for n in notes):
        return "Note already exists."

    notes.append({
        "text": text
    })

    _save_notes(notes)

    return "Note created."
    _save_notes(notes)

    return "Note created."


def show_notes():
    notes = _load_notes()

    if not notes:
        return "No notes found."

    output = []

    for i, note in enumerate(notes, start=1):
        output.append(f"{i}. {note['text']}")

    return "\n".join(output)


def delete_note(index):
    notes = _load_notes()

    index = int(index) - 1

    if index < 0 or index >= len(notes):
        return "Invalid note."

    notes.pop(index)

    _save_notes(notes)

    return "Note deleted."


def search_notes(keyword):
    notes = _load_notes()

    results = []

    for i, note in enumerate(notes, start=1):
        if keyword.lower() in note["text"].lower():
            results.append(f"{i}. {note['text']}")

    if not results:
        return "No matching notes."

    return "\n".join(results)


register(
    name="create_note",
    description="Create a note.",
    parameters={"text": "note text"},
    function=create_note,
)

register(
    name="show_notes",
    description="Show all notes.",
    parameters={},
    function=show_notes,
)

register(
    name="delete_note",
    description="Delete a note.",
    parameters={"index": "note number"},
    function=delete_note,
)

register(
    name="search_notes",
    description="Search notes.",
    parameters={"keyword": "search text"},
    function=search_notes,
)
def delete_note(index):
    notes = _load_notes()

    try:
        index = int(index) - 1
    except:
        return "Invalid note index."

    if index < 0 or index >= len(notes):
        return "Invalid note."

    notes.pop(index)

    _save_notes(notes)

    return "Note deleted."