import os
from datetime import datetime

from brain.tools.tool_registry import register


# =====================================================
# TIME
# =====================================================

def get_time(user_input: str):
    now = datetime.now()
    return now.strftime("%I:%M %p")


# =====================================================
# DATE
# =====================================================

def get_date(user_input: str):
    today = datetime.now()
    return today.strftime("%A, %d %B %Y")


# =====================================================
# LIST FILES
# =====================================================

def list_files(user_input: str):
    files = os.listdir()

    if not files:
        return "Boss, the current directory is empty."

    return "\n".join(files)


# =====================================================
# CURRENT DIRECTORY
# =====================================================

def current_directory(user_input: str):
    return os.getcwd()


# =====================================================
# REGISTER TOOLS
# =====================================================

register("time", get_time)
register("date", get_date)
register("today", get_date)
register("list files", list_files)
register("show files", list_files)
register("current directory", current_directory)
register("where am i", current_directory)