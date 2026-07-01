from brain.rule_engine import detect_rule
from brain.intent_classifier import classify_intent
from brain.tools.router import run_tool
from brain.llm import chat


def execute_intent(user_input: str):

    intent = detect_rule(user_input)

    if intent is None:
        intent = classify_intent(user_input)

    print(f"[Planner] {intent}")

    # Convert intent into a command the router understands
    command_map = {
        "show_notes": "show notes",
        "clear_notes": "clear notes",
        "time": "time",
        "date": "date",
        "list_files": "list files",
        "current_directory": "current directory",
    }

    if intent in command_map:
        return run_tool(command_map[intent])

    if intent == "chat":
        return chat(user_input)

    return run_tool(user_input)