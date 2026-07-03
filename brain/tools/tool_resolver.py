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
}


def resolve_tool(tool_name: str):
    """
    Convert an LLM tool name into a valid DON tool name.
    """
    if not tool_name:
        return None

    return TOOL_ALIASES.get(tool_name.lower(), tool_name)