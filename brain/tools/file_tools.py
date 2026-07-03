import os

from brain.tools.tool_registry import register


# =====================================================
# CREATE FILE
# =====================================================

def create_file(filename: str):
    """
    Create an empty file.
    """

    filename = filename.strip()

    if not filename:
        return "Boss, please provide a filename."

    if os.path.exists(filename):
        return f"Boss, '{filename}' already exists."

    with open(filename, "w", encoding="utf-8"):
        pass

    return f"Boss, created '{filename}'."


# =====================================================
# READ FILE
# =====================================================

def read_file(filename: str):
    """
    Read a file.
    """

    filename = filename.strip()

    if not filename:
        return "Boss, please provide a filename."

    if not os.path.exists(filename):
        return f"Boss, '{filename}' does not exist."

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    if not content.strip():
        return f"Boss, '{filename}' is empty."

    return content


# =====================================================
# WRITE FILE
# =====================================================

def write_file(filename: str, content: str):
    """
    Write content to a file.
    """

    filename = filename.strip()

    if not filename:
        return "Boss, please provide a filename."

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    return f"Boss, wrote to '{filename}'."


# =====================================================
# DELETE FILE
# =====================================================

def delete_file(filename: str):
    """
    Delete a file.
    """

    filename = filename.strip()

    if not filename:
        return "Boss, please provide a filename."

    if not os.path.exists(filename):
        return f"Boss, '{filename}' does not exist."

    os.remove(filename)

    return f"Boss, deleted '{filename}'."


# =====================================================
# RENAME FILE
# =====================================================

def rename_file(old_name: str, new_name: str):
    """
    Rename a file.
    """

    old_name = old_name.strip()
    new_name = new_name.strip()

    if not old_name or not new_name:
        return "Boss, please provide both filenames."

    if not os.path.exists(old_name):
        return f"Boss, '{old_name}' does not exist."

    if os.path.exists(new_name):
        return f"Boss, '{new_name}' already exists."

    os.rename(old_name, new_name)

    return f"Boss, renamed '{old_name}' to '{new_name}'."


# =====================================================
# CREATE FOLDER
# =====================================================

def create_folder(folder_name: str):
    """
    Create a folder.
    """

    folder_name = folder_name.strip()

    if not folder_name:
        return "Boss, please provide a folder name."

    if os.path.exists(folder_name):
        return f"Boss, '{folder_name}' already exists."

    os.makedirs(folder_name)

    return f"Boss, folder '{folder_name}' created."


# =====================================================
# LIST FILES
# =====================================================

def list_files(path: str = "."):
    """
    List files in a directory.
    """

    if not os.path.exists(path):
        return f"Boss, '{path}' does not exist."

    files = os.listdir(path)

    if not files:
        return "Boss, no files found."

    return "\n".join(sorted(files))


# =====================================================
# REGISTER TOOLS
# =====================================================

register(
    name="create_file",
    description="Create a new file.",
    parameters={
        "filename": "Name of the file"
    },
    function=create_file,
)

register(
    name="read_file",
    description="Read a text file.",
    parameters={
        "filename": "Name of the file"
    },
    function=read_file,
)

register(
    name="write_file",
    description="Write text into a file.",
    parameters={
        "filename": "Name of the file",
        "content": "Text to write"
    },
    function=write_file,
)

register(
    name="delete_file",
    description="Delete a file.",
    parameters={
        "filename": "Name of the file"
    },
    function=delete_file,
)

register(
    name="rename_file",
    description="Rename a file.",
    parameters={
        "old_name": "Existing file name",
        "new_name": "New file name"
    },
    function=rename_file,
)

register(
    name="create_folder",
    description="Create a new folder.",
    parameters={
        "folder_name": "Name of the folder"
    },
    function=create_folder,
)

register(
    name="list_files",
    description="List files in a directory.",
    parameters={
        "path": "Directory path (optional)"
    },
    function=list_files,
)