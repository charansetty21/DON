# brain/registry.py

TOOLS = {}


def register_tool(
    name: str,
    description: str,
    examples: list,
    function,
):
    TOOLS[name] = {
        "name": name,
        "description": description,
        "examples": examples,
        "function": function,
    }


def get_tool(name):
    return TOOLS.get(name)


def get_all_tools():
    return TOOLS


def list_tool_descriptions():
    """
    Returns a formatted list of all tools.
    """

    output = ""

    for tool in TOOLS.values():

        output += f"""
Tool: {tool['name']}

Description:
{tool['description']}

Examples:
"""

        for example in tool["examples"]:
            output += f"- {example}\n"

        output += "\n"

    return output