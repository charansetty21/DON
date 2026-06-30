import os

NOTES_FILE = "notes.txt"


def add_note(note: str):
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")

    return "Boss, note saved."


def show_notes():
    if not os.path.exists(NOTES_FILE):
        return "Boss, no notes found."

    with open(NOTES_FILE, "r") as file:
        notes = file.read()

    if notes.strip() == "":
        return "Boss, your notes are empty."

    return notes


def clear_notes():
    with open(NOTES_FILE, "w"):
        pass

    return "Boss, all notes cleared."