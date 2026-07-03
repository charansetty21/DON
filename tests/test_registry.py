from brain.tools.tool_registry import (
    register,
    get_tool,
    list_tools,
)


def hello(name: str):
    return f"Hello {name}"


register(
    name="hello",
    description="Say hello",
    parameters={
        "name": "Person name"
    },
    function=hello,
)

print(list_tools())
print(get_tool("hello"))