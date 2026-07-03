TOOLS = {}


def register(name, description="", parameters=None, function=None):
    """
    Register a tool.
    """

    if parameters is None:
        parameters = {}

    TOOLS[name] = {
        "name": name,
        "description": description,
        "parameters": parameters,
        "function": function,
    }


def get_tool(name):
    """
    Return a registered tool.
    """
    return TOOLS.get(name)


def get_tools():
    """
    Return all registered tools.
    """
    return TOOLS