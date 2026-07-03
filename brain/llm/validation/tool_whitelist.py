from brain.tools.tool_registry import registry


def is_valid_tool(tool_name: str) -> bool:
    """
    Ensures LLM cannot invent fake tools.
    """

    return registry.get(tool_name) is not None