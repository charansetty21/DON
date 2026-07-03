from brain.tools.tool_registry import get_tool

import brain.tools
def run_tool(user_input: str):
    text = user_input.lower()

    for command, function in get_tools().items():
        if text.startswith(command):
            return function(user_input)

    return None
