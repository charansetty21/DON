from brain.llm.client import LLMClient
import json

llm = LLMClient()

SYSTEM_PROMPT = """
You are DON's task planner.

Your job is to convert a user's request into REAL executable tasks.

Rules:
- Return ONLY valid JSON.
- Do NOT analyze the sentence.
- Do NOT identify intent.
- Do NOT explain your reasoning.
- Do NOT generate thinking steps.
- Every task must describe something DON can actually do.

Examples:

User: hey don
{
  "tasks": [
    "Reply with a friendly greeting."
  ]
}

User: what time is it
{
  "tasks": [
    "Get the current time."
  ]
}

User: open calculator
{
  "tasks": [
    "Open the Calculator application."
  ]
}

User: create a note saying buy milk
{
  "tasks": [
    "Create a note with the text 'buy milk'."
  ]
}
"""

def decompose_goal(user_input: str):
    """
    Converts a high-level goal into executable tasks.
    """

    prompt = SYSTEM_PROMPT + f"\n\nUser: {user_input}"

    raw = llm.generate(prompt)

    try:
        data = json.loads(raw)
        return data.get("tasks", [])
    except Exception:
        return [user_input]