import brain.tools.web_tools

from brain.tools.tool_registry import get_tool


tool = get_tool("web_search")

print(tool["function"]("Latest AI news"))