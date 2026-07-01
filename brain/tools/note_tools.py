import os

from brain.tools.tool_registry import register
from brain.registry import register_tool
NOTES_FILE = "notes.txt"


# =====================================================
# ADD NOTE
# =====================================================

def add_note(user_input: str):
    note = user_input[len("add note"):].strip()

    if not note:
        return "Boss, what should I save?"

    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")

    return "Boss, note saved."


# =====================================================
# SHOW NOTES
# =====================================================

def show_notes(user_input: str):
    if not os.path.exists(NOTES_FILE):
        return "Boss, no notes found."

    with open(NOTES_FILE, "r") as file:
        notes = file.read()

    if not notes.strip():
        return "Boss, your notes are empty."

    return notes


# =====================================================
# CLEAR NOTES
# =====================================================

def clear_notes(user_input: str):
    with open(NOTES_FILE, "w"):
        pass

    return "Boss, all notes cleared."


register_tool(
    name="add_note",
    description="Save a note for the user.",
    examples=[
        "add note buy milk",
        "remember buy milk",
        "save this note"
    ],
    function=add_note,
)

register_tool(
    name="show_notes",
    description="Display all saved notes.",
    examples=[
        "show notes",
        "show my notes",
        "display notes"
    ],
    function=show_notes,
)

register_tool(
    name="clear_notes",
    description="Delete all notes.",
    examples=[
        "clear notes",
        "delete all notes",
        "remove notes"
    ],
    function=clear_notes,
)