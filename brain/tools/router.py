from brain.tools.tool_registry import get_tools

# Import tool modules so they register themselves
import brain.tools.system_tools
import brain.tools.file_tools
import brain.tools.note_tools
import brain.tools.web_tools
import brain.tools.app_tools


def run_tool(user_input: str):
    text = user_input.lower()

    for command, function in get_tools().items():
        if text.startswith(command):
            return function(user_input)

    return None