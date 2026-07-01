import os

from brain.tools.tool_registry import register

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


# =====================================================
# REGISTER TOOLS
# =====================================================

register("add note", add_note)
register("show notes", show_notes)
register("clear notes", clear_notes)