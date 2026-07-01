from brain.tools.tool_registry import get_tools

# Import modules so they register their tools
import brain.tools.system_tools
import brain.tools.file_tools
import brain.tools.note_tools
import brain.tools.web_tools

from brain.tools.app_tools import open_application
from brain.tools.note_tools import add_note


def run_tool(user_input: str):
    text = user_input.lower()

    # =====================================================
    # TOOL REGISTRY
    # =====================================================
    tools = get_tools()

    for command, function in tools.items():
        if text.startswith(command):
            return function(user_input)

    # =====================================================

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
    # NO TOOL MATCHED
    # =====================================================
    return None