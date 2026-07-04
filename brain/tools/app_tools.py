import os
import platform
from brain.tools.tool_registry import register


def open_app(name: str):
    system = platform.system()

    try:
        # macOS
        if system == "Darwin":
            os.system(f"open -a '{name}'")

        # Windows
        elif system == "Windows":
            os.system(f"start {name}")

        # Linux
        else:
            os.system(name)

        return f"Opened {name}"

    except Exception as e:
        return f"Failed to open {name}: {str(e)}"


register(
    name="open_app",
    description="Open applications like calculator, chrome, vscode",
    parameters={"name": "application name"},
    function=open_app,
)