from brain.tools.base import Tool
from brain.memory.memory import memory


class RecallTool(Tool):
    name = "recall_memory"
    description = "Searches semantic memory"

    def run(self, query: str):
        results = memory.rag.search(query)

        if not results:
            return "No relevant memory found."

        return results