# brain/rule_engine.py

def detect_rule(user_input: str):
    """
    Detect obvious tool requests using simple rules.
    Returns the intent or None.
    """

    text = user_input.lower()

    # -----------------------
    # Notes
    # -----------------------

    if "note" in text:
        if any(word in text for word in [
            "show",
            "display",
            "read",
            "list",
            "see"
        ]):
            return "show_notes"

        if any(word in text for word in [
            "add",
            "remember",
            "save",
            "store"
        ]):
            return "add_note"

        if any(word in text for word in [
            "clear",
            "delete",
            "remove"
        ]):
            return "clear_notes"

    # -----------------------
    # Apps
    # -----------------------

    if any(word in text for word in [
        "open",
        "launch",
        "start",
        "run"
    ]):
        return "open_app"

    # -----------------------
    # Files
    # -----------------------

    if "create file" in text:
        return "create_file"

    if "read file" in text:
        return "read_file"

    if "delete file" in text:
        return "delete_file"

    if "rename file" in text:
        return "rename_file"

    if "create folder" in text:
        return "create_folder"

    # -----------------------
    # System
    # -----------------------

    if "time" in text:
        return "time"

    if "date" in text or "today" in text:
        return "date"

    if "current directory" in text:
        return "current_directory"

    if "list files" in text:
        return "list_files"

    return None