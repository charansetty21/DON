from datetime import datetime
import os


def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.now().strftime("%d %B %Y")


def list_files():
    files = os.listdir(".")
    return "\n".join(files)


def current_directory():
    return os.getcwd()