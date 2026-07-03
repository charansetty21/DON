import brain.tools.note_tools

from brain.tools.tool_registry import get_tool

tool = get_tool("add_note")

result = tool["function"](note="Buy milk")

print(result)