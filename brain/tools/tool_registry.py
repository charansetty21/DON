"""
DON Tool Registry

Every tool registers itself here.

The registry stores:

- name
- description
- parameters
- function
"""

TOOLS = {}


def register(
    name: str,
    description: str,
    parameters: dict,
    function,
):
    """
    Register a tool.

    Example:

    register(
        name="open_application",
        description="Open an installed application",
        parameters={
            "app":"Application name"
        },
        function=open_application
    )
    """

    TOOLS[name] = {
        "name": name,
        "description": description,
        "parameters": parameters,
        "function": function,
    }


def get_tool(name: str):
    return TOOLS.get(name)


def get_tools():
    return TOOLS


def list_tools():
    return list(TOOLS.keys())