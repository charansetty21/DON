import brain.tools

from brain.tools.tool_registry import list_tools

print("=" * 50)
print("REGISTERED TOOLS")
print("=" * 50)

for tool in list_tools():
    print(tool["name"])