import os
import platform
from datetime import datetime

from brain.tools.tool_registry import register


# =====================================================
# CURRENT TIME
# =====================================================

def current_time():
    """
    Return the current system time.
    """
    return datetime.now().strftime("%I:%M:%S %p")


# =====================================================
# CURRENT DATE
# =====================================================

def current_date():
    """
    Return the current system date.
    """
    return datetime.now().strftime("%d %B %Y")


# =====================================================
# CURRENT DIRECTORY
# =====================================================

def current_directory():
    """
    Return the current working directory.
    """
    return os.getcwd()


# =====================================================
# LIST DIRECTORY
# =====================================================

def list_directory(path="."):
    """
    List files and folders in a directory.
    """

    if not os.path.exists(path):
        return f"Boss, '{path}' does not exist."

    items = sorted(os.listdir(path))

    if not items:
        return "Boss, the directory is empty."

    return "\n".join(items)


# =====================================================
# SYSTEM INFO
# =====================================================

def system_info():
    """
    Return basic system information.
    """

    info = [
        f"Operating System : {platform.system()}",
        f"Release          : {platform.release()}",
        f"Machine          : {platform.machine()}",
        f"Processor        : {platform.processor()}",
        f"Python Version   : {platform.python_version()}",
    ]

    return "\n".join(info)


# =====================================================
# REGISTER TOOLS
# =====================================================

register(
    name="current_time",
    description="Get the current system time.",
    parameters={},
    function=current_time,
)

register(
    name="current_date",
    description="Get the current system date.",
    parameters={},
    function=current_date,
)

register(
    name="current_directory",
    description="Get the current working directory.",
    parameters={},
    function=current_directory,
)

register(
    name="list_directory",
    description="List files and folders in a directory.",
    parameters={
        "path": "Directory path (optional)"
    },
    function=list_directory,
)

register(
    name="system_info",
    description="Get operating system information.",
    parameters={},
    function=system_info,
)