from brain.llm.client import LLMClient
import json


llm = LLMClient()


SYSTEM_PROMPT = """
You are DON Dependency Planner.

Convert tasks into a dependency graph.

Rules:
- Output ONLY JSON
- Each task may depend on previous tasks
- If no dependency, leave empty list

Format:

{
  "tasks": [
    {
      "name": "task 1",
      "depends_on": []
    },
    {
      "name": "task 2",
      "depends_on": ["task 1"]
    }
  ]
}
"""


def build_dependency_graph(tasks):
    """
    Converts flat tasks into dependency-aware structure.
    """

    prompt = SYSTEM_PROMPT + "\nTasks:\n" + str(tasks)

    raw = llm.generate(prompt)

    try:
        data = json.loads(raw)
        return data.get("tasks", [])
    except Exception:
        # fallback → no dependencies
        return [{"name": t, "depends_on": []} for t in tasks]