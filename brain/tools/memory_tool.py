from brain.tools.base import Tool
from brain.memory.memory import memory


class SaveMemoryTool(Tool):
    name = "save_memory"
    description = "Save a key-value memory"

    def run(self, key: str, value: str):
        memory.set_long(key, value)
        return f"Saved memory: {key}"