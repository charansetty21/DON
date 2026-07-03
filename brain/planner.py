from brain.rule_engine import detect_rule
from brain.intent_classifier import classify_intent
from brain.executor import execute


def execute_intent(user_input: str):
    """
    Planner:
    Decides WHAT should happen.
    """

    intent = detect_rule(user_input)

    if intent is None:
        intent = classify_intent(user_input)

    print(f"[Planner] {intent}")

    command_map = {
        "show_notes": "show notes",
        "clear_notes": "clear notes",
        "time": "time",
        "date": "date",
        "list_files": "list files",
        "current_directory": "current directory",
    }

    command = command_map.get(intent, user_input)

    return execute(intent, command)