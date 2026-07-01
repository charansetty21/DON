# brain/registry.py

TOOLS = {}


def register_tool(
    name: str,
    description: str,
    examples: list,
    function,
):
    """
    Register a tool.
    """

    TOOLS[name] = {
        "description": description,
        "examples": examples,
        "function": function,
    }


def get_tools():
    return TOOLS


def get_tool(name):
    return TOOLS.get(name)