import json


def extract_json(text: str):
    """
    Tries to safely extract JSON from LLM output.
    """

    try:
        return json.loads(text)
    except Exception:
        pass

    # fallback: try to find JSON block
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        return None

    try:
        return json.loads(text[start:end+1])
    except Exception:
        return None


def is_valid_plan(data: dict) -> bool:
    """
    Basic schema validation for DON plans.
    """

    if not isinstance(data, dict):
        return False

    if "action" not in data:
        return False

    if data["action"] not in ["tool", "sequence", "chat"]:
        return False

    return True