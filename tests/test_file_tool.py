import brain.tools.file_tools

from brain.tools.tool_registry import get_tool


print("Registered Tools:")
print("-" * 40)

for tool in [
    "create_file",
    "read_file",
    "write_file",
    "delete_file",
    "rename_file",
    "create_folder",
    "list_files",
]:
    print(get_tool(tool)["name"])


print("\nCreating file...")
tool = get_tool("create_file")
print(tool["function"]("demo.txt"))

print("\nWriting file...")
tool = get_tool("write_file")
print(tool["function"]("demo.txt", "Hello Boss"))

print("\nReading file...")
tool = get_tool("read_file")
print(tool["function"]("demo.txt"))

print("\nListing files...")
tool = get_tool("list_files")
print(tool["function"]())

print("\nRenaming file...")
tool = get_tool("rename_file")
print(tool["function"]("demo.txt", "example.txt"))

print("\nDeleting file...")
tool = get_tool("delete_file")
print(tool["function"]("example.txt"))

print("\nCreating folder...")
tool = get_tool("create_folder")
print(tool["function"]("DemoFolder"))