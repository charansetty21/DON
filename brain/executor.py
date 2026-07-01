# brain/executor.py

from brain.registry import get_tool


def execute(tool_name, user_input):
    """
    Execute a registered tool.
    """

    tool = get_tool(tool_name)

    if tool is None:
        return None

    return tool["function"](user_input)