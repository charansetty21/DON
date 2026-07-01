from brain.registry import get_tool


def execute(tool_name, user_input=""):
    tool = get_tool(tool_name)

    if tool is None:
        return None

    return tool["function"](user_input)