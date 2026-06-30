from brain.tools.system_tools import (
    get_time,
    get_date,
    list_files,
    current_directory,
)

from brain.tools.app_tools import open_application

from brain.tools.file_tools import (
    create_file,
    read_file,
    write_file,
    delete_file,
    rename_file,
    create_folder,
)

from brain.tools.note_tools import (
    add_note,
    show_notes,
    clear_notes,
)


def run_tool(user_input: str):
    text = user_input.lower().strip()

    # =====================================================
    # TIME
    # =====================================================
    if "time" in text:
        return get_time()

    # =====================================================
    # DATE
    # =====================================================
    if "date" in text or "today" in text:
        return get_date()

    # =====================================================
    # LIST FILES
    # =====================================================
    if "list files" in text or "show files" in text:
        return list_files()

    # =====================================================
    # CURRENT DIRECTORY
    # =====================================================
    if "current directory" in text or "where am i" in text:
        return current_directory()

    # =====================================================
    # NOTES
    # =====================================================
    if text.startswith("add note"):
        note = user_input[len("add note"):].strip()

        if not note:
            return "Boss, what should I save?"

        return add_note(note)

    if text == "show notes":
        return show_notes()

    if text == "clear notes":
        return clear_notes()

    # =====================================================
    # OPEN APPLICATION
    # =====================================================
    if text.startswith("open "):
        app = user_input[5:].strip()

        app_map = {
            "chrome": "Google Chrome",
            "google chrome": "Google Chrome",
            "google": "Google Chrome",
            "calculator": "Calculator",
            "terminal": "Terminal",
            "vs code": "Visual Studio Code",
            "vscode": "Visual Studio Code",
            "notes": "Notes",
            "calendar": "Calendar",
            "mail": "Mail",
        }

        app_name = app_map.get(app.lower(), app)

        return open_application(app_name)

    # =====================================================
    # CREATE FILE
    # =====================================================
    if text.startswith("create file "):
        filename = user_input[12:].strip()

        if not filename:
            return "Boss, please provide a filename."

        return create_file(filename)

    # =====================================================
    # READ FILE
    # =====================================================
    if text.startswith("read file "):
        filename = user_input[10:].strip()

        if not filename:
            return "Boss, please provide a filename."

        return read_file(filename)

    # =====================================================
    # WRITE FILE
    # =====================================================
    if text.startswith("write file "):
        command = user_input[11:].strip()

        parts = command.split(" ", 1)

        if len(parts) != 2:
            return "Usage: Write file <filename> <content>"

        filename = parts[0]
        content = parts[1]

        return write_file(filename, content)

    # =====================================================
    # DELETE FILE
    # =====================================================
    if text.startswith("delete file "):
        filename = user_input[12:].strip()

        if not filename:
            return "Boss, please provide a filename."

        return delete_file(filename)

    # =====================================================
    # RENAME FILE
    # =====================================================
    if text.startswith("rename file "):
        command = user_input[12:].strip()

        if " to " not in command:
            return "Usage: Rename file <old_name> to <new_name>"

        old_name, new_name = command.split(" to ", 1)

        return rename_file(old_name.strip(), new_name.strip())

    # =====================================================
    # CREATE FOLDER
    # =====================================================
    if text.startswith("create folder "):
        folder_name = user_input[14:].strip()

        if not folder_name:
            return "Boss, please provide a folder name."

        return create_folder(folder_name)

    # =====================================================
    # NO TOOL MATCHED
    # =====================================================
    return None