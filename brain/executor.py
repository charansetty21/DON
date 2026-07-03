from brain.tools.tool_registry import get_tool


def execute_plan(plan: dict):
    action = plan.get("action")

    if action == "chat":
        return None

    if action == "tool":

        tool_name = plan.get("tool")

        tool = get_tool(tool_name)

        if tool is None:
            return f"Tool '{tool_name}' not found."

        arguments = plan.get("arguments", {})

        try:
            return tool(**arguments)

        except TypeError:
            return tool()

    return "Unknown action."