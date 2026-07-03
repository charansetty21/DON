import os

from brain.tools.tool_registry import register

NOTES_FILE = "notes.txt"


# =====================================================
# ADD NOTE
# =====================================================

def add_note(note: str):
    """
    Save a note to the notes file.
    """

    note = note.strip()

    if not note:
        return "Boss, what should I save?"

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    return "Boss, note saved."


# =====================================================
# SHOW NOTES
# =====================================================

def show_notes():
    """
    Display all saved notes.
    """

    if not os.path.exists(NOTES_FILE):
        return "Boss, no notes found."

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.read().strip()

    if not notes:
        return "Boss, your notes are empty."

    return notes


# =====================================================
# CLEAR NOTES
# =====================================================

def clear_notes():
    """
    Delete all saved notes.
    """

    with open(NOTES_FILE, "w", encoding="utf-8"):
        pass

    return "Boss, all notes cleared."


# =====================================================
# REGISTER TOOLS
# =====================================================

register(
    name="add_note",
    description="Save a note for the user.",
    parameters={
        "note": "Text to save as a note"
    },
    function=add_note,
)

register(
    name="show_notes",
    description="Display all saved notes.",
    parameters={},
    function=show_notes,
)

register(
    name="clear_notes",
    description="Delete all saved notes.",
    parameters={},
    function=clear_notes,
)