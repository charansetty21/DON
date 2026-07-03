import brain.tools.system_tools

from brain.tools.tool_registry import get_tool


print("=" * 50)
print("SYSTEM TOOL TESTS")
print("=" * 50)

print("\nCurrent Time")
print(get_tool("current_time")["function"]())

print("\nCurrent Date")
print(get_tool("current_date")["function"]())

print("\nCurrent Directory")
print(get_tool("current_directory")["function"]())

print("\nDirectory Contents")
print(get_tool("list_directory")["function"]())

print("\nSystem Information")
print(get_tool("system_info")["function"]())

print("\nAll tests passed.")