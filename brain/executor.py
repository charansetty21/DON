from brain.tools.tool_registry import get_tool
from brain.tools.tool_resolver import resolve_tool


def execute_plan(plan):
    """
    Executes a plan returned by the planner.

    Plan format:
    {
        "action": "chat" | "tool",
        "message": "...",
        "tool": "...",
        "arguments": {}
    }
    """

    action = plan.get("action")

    # -------------------------
    # CHAT
    # -------------------------
    if action == "chat":
        return plan.get(
            "message",
            "I am not sure how to help with that."
        )

    # -------------------------
    # TOOL
    # -------------------------
    if action == "tool":

        # Resolve LLM tool aliases
        tool_name = resolve_tool(plan.get("tool"))

        if not tool_name:
            return "No tool specified in plan."

        tool = get_tool(tool_name)

        if tool is None:
            return f"Tool '{tool_name}' not found."

        function = tool.get("function")

        if function is None:
            return f"Tool '{tool_name}' has no executable function."

        arguments = plan.get("arguments", {})

        try:
            if isinstance(arguments, dict):
                return function(**arguments)
            else:
                return function()

        except Exception as e:
            return f"Execution error in tool '{tool_name}': {e}"

    # -------------------------
    # UNKNOWN ACTION
    # -------------------------
    return f"Unknown action: {action}"