import brain.tools.app_tools

from brain.tools.tool_registry import get_tool

tool = get_tool("open_application")

print(tool)

result = tool["function"](app="chrome")

print(result)
result = tool["function"](app="calculator")
print(result)