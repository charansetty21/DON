"""
Maps LLM-generated tool names to DON's internal tool names.
"""

TOOL_ALIASES = {
    # Time
    "time": "current_time",
    "current_time": "current_time",
    "datetime": "current_time",
    "clock": "current_time",

    # Date
    "date": "current_date",
    "today": "current_date",
    "current_date": "current_date",

    # Files
    "ls": "list_directory",
    "list_files": "list_directory",
    "list_directory": "list_directory",
    "files": "list_directory",

    # Directory
    "pwd": "current_directory",
    "current_directory": "current_directory",
    "directory": "current_directory",

    # Notes
    "create note": "create_note",
    "create_note": "create_note",
    "note create": "create_note",

    "show notes": "show_notes",
    "list notes": "show_notes",
    "notes": "show_notes",

    "delete note": "delete_note",
    "remove note": "delete_note",

    "search notes": "search_notes",
    "find notes": "search_notes",
# Apps
"open calculator": "open_app",
"calculator": "open_app",
"open chrome": "open_app",
"chrome": "open_app",
"open vscode": "open_app",
"vscode": "open_app",
"open app": "open_app",

# ==========================
# File Tools
# ==========================

# Create
"create file": "create_file",
"new file": "create_file",
"make file": "create_file",

# Read
"read file": "read_file",
"open file": "read_file",
"show file": "read_file",

# Write
"write file": "write_file",
"save file": "write_file",

# Delete
"delete file": "delete_file",
"remove file": "delete_file",

# Rename
"rename file": "rename_file",

# Copy
"copy file": "copy_file",

# Move
"move file": "move_file",
}


def resolve_tool(tool_name: str):
    """
    Convert an LLM tool name into a valid DON tool name.
    """
    if not tool_name:
        return None

    return TOOL_ALIASES.get(tool_name.lower(), tool_name)