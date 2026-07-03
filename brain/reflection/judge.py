from brain.llm.client import LLMClient
import json


llm = LLMClient()


SYSTEM_PROMPT = """
You are a strict evaluation system for an AI assistant called DON.

Your job:
Decide if the task was SUCCESS or FAILURE.

Return ONLY JSON:

{
  "status": "success" | "failure",
  "reason": "short explanation"
}

Rules:
- Be strict
- If output is incomplete → failure
- If output does not match user intent → failure
- Otherwise → success
"""


def judge(user_input: str, result) -> dict:
    """
    LLM-based semantic evaluation.
    """

    prompt = f"""
User Request:
{user_input}

DON Output:
{result}

Evaluate now.
"""

    raw = llm.generate(SYSTEM_PROMPT + prompt)

    try:
        return json.loads(raw)
    except Exception:
        return {
            "status": "failure",
            "reason": "invalid judge output"
        }