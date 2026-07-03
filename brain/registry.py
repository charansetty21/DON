TOOLS = {}


def register(name: str, function):
    """
    Register a tool using a unique tool name.
    """
    TOOLS[name] = function


def get_tool(name: str):
    """
    Get a tool by name.
    """
    return TOOLS.get(name)


def get_tools():
    return TOOLS