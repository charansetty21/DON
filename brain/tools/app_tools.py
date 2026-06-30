import subprocess


def open_application(app_name: str):
    """
    Opens any installed macOS application.
    """

    try:
        subprocess.run(
            ["open", "-a", app_name],
            check=True
        )
        return f"Opening {app_name}."

    except subprocess.CalledProcessError:
        return f"Boss, I couldn't find '{app_name}'."