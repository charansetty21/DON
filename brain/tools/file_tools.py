import os


def create_file(filename: str):
    if os.path.exists(filename):
        return f"Boss, '{filename}' already exists."

    with open(filename, "w"):
        pass

    return f"Boss, '{filename}' has been created."


def read_file(filename: str):
    if not os.path.exists(filename):
        return f"Boss, '{filename}' does not exist."

    with open(filename, "r") as file:
        content = file.read()

    if content.strip() == "":
        return f"Boss, '{filename}' is empty."

    return content


def write_file(filename: str, content: str):
    with open(filename, "w") as file:
        file.write(content)

    return f"Boss, wrote to '{filename}'."


def delete_file(filename: str):
    if not os.path.exists(filename):
        return f"Boss, '{filename}' does not exist."

    os.remove(filename)

    return f"Boss, '{filename}' has been deleted."


def rename_file(old_name: str, new_name: str):
    if not os.path.exists(old_name):
        return f"Boss, '{old_name}' does not exist."

    os.rename(old_name, new_name)

    return f"Boss, renamed '{old_name}' to '{new_name}'."


def create_folder(folder_name: str):
    if os.path.exists(folder_name):
        return f"Boss, '{folder_name}' already exists."

    os.makedirs(folder_name)

    return f"Boss, folder '{folder_name}' created."