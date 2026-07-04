import os
import shutil

from brain.tools.tool_registry import register


# =====================================================
# CREATE FILE
# =====================================================

def create_file(path):
    try:
        if os.path.exists(path):
            return f"File '{path}' already exists."

        with open(path, "w", encoding="utf-8"):
            pass

        return f"File '{path}' created."

    except Exception as e:
        return str(e)


# =====================================================
# READ FILE
# =====================================================

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return str(e)


# =====================================================
# WRITE FILE
# =====================================================

def write_file(path, text):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

        return f"Written to '{path}'."

    except Exception as e:
        return str(e)


# =====================================================
# DELETE FILE
# =====================================================

def delete_file(path):
    try:
        os.remove(path)
        return f"Deleted '{path}'."

    except Exception as e:
        return str(e)


# =====================================================
# RENAME FILE
# =====================================================

def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        return f"Renamed '{old_path}' to '{new_path}'."

    except Exception as e:
        return str(e)


# =====================================================
# COPY FILE
# =====================================================

def copy_file(source, destination):
    try:
        shutil.copy2(source, destination)
        return f"Copied '{source}' to '{destination}'."

    except Exception as e:
        return str(e)


# =====================================================
# MOVE FILE
# =====================================================

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        return f"Moved '{source}' to '{destination}'."

    except Exception as e:
        return str(e)


# =====================================================
# REGISTER TOOLS
# =====================================================

register(
    name="create_file",
    description="Create a new file.",
    parameters={"path": "File path"},
    function=create_file,
)

register(
    name="read_file",
    description="Read a file.",
    parameters={"path": "File path"},
    function=read_file,
)

register(
    name="write_file",
    description="Write text into a file.",
    parameters={
        "path": "File path",
        "text": "Text to write",
    },
    function=write_file,
)

register(
    name="delete_file",
    description="Delete a file.",
    parameters={"path": "File path"},
    function=delete_file,
)

register(
    name="rename_file",
    description="Rename a file.",
    parameters={
        "old_path": "Existing file",
        "new_path": "New file name",
    },
    function=rename_file,
)

register(
    name="copy_file",
    description="Copy a file.",
    parameters={
        "source": "Source file",
        "destination": "Destination",
    },
    function=copy_file,
)

register(
    name="move_file",
    description="Move a file.",
    parameters={
        "source": "Source file",
        "destination": "Destination",
    },
    function=move_file,
)