from brain.tools.tool_registry import get_tool
from brain.tools.tool_resolver import resolve_tool


def execute_plan(plan):
    """
    Executes a plan returned by the planner.
    """

    # -------------------------
    # CHAT ACTION
    # -------------------------
    if plan.get("action") == "chat":
        return plan.get("message", "I am not sure how to help with that.")

    # -------------------------
    # TOOL ACTION
    # -------------------------
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

    # =====================================================
    # NOTES NORMALIZATION
    # =====================================================

    if tool_name == "create_note":

        text = (
            arguments.get("text")
            or arguments.get("note")
            or arguments.get("content")
            or ""
        )

        arguments = {
            "text": text
        }

    elif tool_name == "delete_note":

        index = (
            arguments.get("index")
            or arguments.get("note_id")
            or 1
        )

        arguments = {
            "index": index
        }

    elif tool_name == "search_notes":

        keyword = (
            arguments.get("keyword")
            or arguments.get("query")
            or arguments.get("text")
            or ""
        )

        arguments = {
            "keyword": keyword
        }

    # =====================================================
    # APP NORMALIZATION
    # =====================================================

    elif tool_name == "open_app":

        name = (
            arguments.get("name")
            or arguments.get("app")
            or arguments.get("application")
            or arguments.get("tool_name")
            or ""
        )

        arguments = {
            "name": name
        }

    # =====================================================
    # FILE NORMALIZATION
    # =====================================================

    elif tool_name == "create_file":

        path = (
            arguments.get("path")
            or arguments.get("file")
            or arguments.get("filename")
            or arguments.get("file_name")
            or arguments.get("name")
            or ""
        )

        arguments = {
            "path": path
        }

    elif tool_name == "read_file":

        path = (
            arguments.get("path")
            or arguments.get("file")
            or arguments.get("filename")
            or arguments.get("file_name")
            or ""
        )

        arguments = {
            "path": path
        }

    elif tool_name == "write_file":

        path = (
            arguments.get("path")
            or arguments.get("file")
            or arguments.get("filename")
            or arguments.get("file_name")
            or arguments.get("name")
            or ""
        )

        text = (
            arguments.get("text")
            or arguments.get("content")
            or arguments.get("data")
            or ""
        )

        arguments = {
            "path": path,
            "text": text
        }

    elif tool_name == "delete_file":

        path = (
            arguments.get("path")
            or arguments.get("file")
            or arguments.get("filename")
            or arguments.get("file_name")
            or arguments.get("name")
            or ""
        )

        arguments = {
            "path": path
        }

    elif tool_name == "rename_file":

        old_path = (
            arguments.get("old_path")
            or arguments.get("source")
            or arguments.get("from")
            or ""
        )

        new_path = (
            arguments.get("new_path")
            or arguments.get("destination")
            or arguments.get("to")
            or ""
        )

        arguments = {
            "old_path": old_path,
            "new_path": new_path
        }

    elif tool_name == "copy_file":

        source = (
            arguments.get("source")
            or arguments.get("from")
            or ""
        )

        destination = (
            arguments.get("destination")
            or arguments.get("to")
            or ""
        )

        arguments = {
            "source": source,
            "destination": destination
        }

    elif tool_name == "move_file":

        source = (
            arguments.get("source")
            or arguments.get("from")
            or ""
        )

        destination = (
            arguments.get("destination")
            or arguments.get("to")
            or ""
        )

        arguments = {
            "source": source,
            "destination": destination
        }
    # =====================================================
    # EXECUTE TOOL
    # =====================================================

    try:
        return function(**arguments)

    except Exception as e:
        return f"Execution error in tool '{tool_name}': {str(e)}"