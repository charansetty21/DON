import subprocess

from brain.tools.tool_registry import register


APP_MAP = {
    "chrome": "Google Chrome",
    "google chrome": "Google Chrome",
    "google": "Google Chrome",
    "calculator": "Calculator",
    "terminal": "Terminal",
    "vs code": "Visual Studio Code",
    "vscode": "Visual Studio Code",
    "notes": "Notes",
    "calendar": "Calendar",
    "mail": "Mail",
}


def open_application(app: str):
    """
    Open an installed macOS application.
    """

    app_name = APP_MAP.get(app.lower(), app)

    try:
        subprocess.run(
            ["open", "-a", app_name],
            check=True
        )

        return f"Opening {app_name}."

    except subprocess.CalledProcessError:
        return f"Boss, I couldn't find '{app_name}'."


register(
    name="open_application",
    description="Open an installed application on macOS.",
    parameters={
        "app": "Application name"
    },
    function=open_application,
)