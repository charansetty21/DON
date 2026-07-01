import os

from brain.tools.tool_registry import register


# =====================================================
# CREATE FILE
# =====================================================

def create_file(user_input: str):
    filename = user_input[len("create file"):].strip()

    if not filename:
        return "Boss, please provide a filename."

    if os.path.exists(filename):
        return f"Boss, '{filename}' already exists."

    with open(filename, "w"):
        pass

    return f"Boss, created '{filename}'."


# =====================================================
# READ FILE
# =====================================================

def read_file(user_input: str):
    filename = user_input[len("read file"):].strip()

    if not filename:
        return "Boss, please provide a filename."

    if not os.path.exists(filename):
        return f"Boss, '{filename}' does not exist."

    with open(filename, "r") as file:
        content = file.read()

    if not content.strip():
        return f"Boss, '{filename}' is empty."

    return content


# =====================================================
# WRITE FILE
# =====================================================

def write_file(user_input: str):
    command = user_input[len("write file"):].strip()

    parts = command.split(" ", 1)

    if len(parts) != 2:
        return "Usage: write file <filename> <content>"

    filename = parts[0]
    content = parts[1]

    with open(filename, "w") as file:
        file.write(content)

    return f"Boss, wrote to '{filename}'."


# =====================================================
# DELETE FILE
# =====================================================

def delete_file(user_input: str):
    filename = user_input[len("delete file"):].strip()

    if not filename:
        return "Boss, please provide a filename."

    if not os.path.exists(filename):
        return f"Boss, '{filename}' does not exist."

    os.remove(filename)

    return f"Boss, deleted '{filename}'."


# =====================================================
# RENAME FILE
# =====================================================

def rename_file(user_input: str):
    command = user_input[len("rename file"):].strip()

    if " to " not in command:
        return "Usage: rename file <old_name> to <new_name>"

    old_name, new_name = command.split(" to ", 1)

    old_name = old_name.strip()
    new_name = new_name.strip()

    if not os.path.exists(old_name):
        return f"Boss, '{old_name}' does not exist."

    os.rename(old_name, new_name)

    return f"Boss, renamed '{old_name}' to '{new_name}'."


# =====================================================
# CREATE FOLDER
# =====================================================

def create_folder(user_input: str):
    folder_name = user_input[len("create folder"):].strip()

    if not folder_name:
        return "Boss, please provide a folder name."

    if os.path.exists(folder_name):
        return f"Boss, '{folder_name}' already exists."

    os.makedirs(folder_name)

    return f"Boss, folder '{folder_name}' created."


# =====================================================
# REGISTER TOOLS
# =====================================================

register("create file", create_file)
register("read file", read_file)
register("write file", write_file)
register("delete file", delete_file)
register("rename file", rename_file)
register("create folder", create_folder)