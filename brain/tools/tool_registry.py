# brain/tools/tool_registry.py

TOOLS = {}


def register(command: str, function):
    """
    Register a tool.

    command: Command prefix (e.g. "create file")
    function: Function that receives the full user command
    """
    TOOLS[command.lower()] = function


def get_tools():
    return TOOLS