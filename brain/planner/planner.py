import json

from brain.llm.client import LLMClient
from brain.tools.tool_registry import get_tools

llm = LLMClient()


def build_plan(user_input: str):

    tools = get_tools()

    tool_list = ""
    for name, tool in tools.items():
        tool_list += f'- "{name}" : {tool["description"]}\n'

    prompt = f"""
You are DON's execution planner.

You MUST answer using EXACTLY ONE JSON object.

The ONLY valid actions are:

1.
{{
    "action":"chat",
    "message":"text"
}}

2.
{{
    "action":"tool",
    "tool":"tool_name",
    "arguments":{{}}
}}

Rules:

- Return ONLY valid JSON.
- Never explain.
- Never use markdown.
- Never invent tool names.
- The tool MUST be one of the available tools.

NOTES

- "create note" -> create_note
- "add note" -> create_note
- "show notes" -> show_notes
- "list notes" -> show_notes
- "search notes" -> search_notes
- "find notes" -> search_notes
- "delete note" -> delete_note

FILES

- "create file" -> create_file
- "read file" -> read_file
- "open file" -> read_file
- "write to file" -> write_file
- "write ... to file" -> write_file
- "delete file" -> delete_file
- "rename file" -> rename_file
- "copy file" -> copy_file
- "move file" -> move_file

APPS

- "open calculator" -> open_app
- "open chrome" -> open_app
- "open vscode" -> open_app

SYSTEM

- "what time is it" -> current_time
- "today's date" -> current_date
- "current directory" -> current_directory
- "list files" -> list_directory

Return ONLY a JSON object.

User request:
{user_input}
{user_input}
"""

    raw = llm.generate(prompt).strip()

    print("\n========== RAW ==========")
    print(raw)
    print("=========================\n")

    # Remove markdown fences if the model adds them
    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        plan = json.loads(raw)

        # Validate action
        if plan.get("action") not in ("chat", "tool"):
            raise ValueError(f"Invalid action: {plan.get('action')}")

        return plan

    except Exception as e:
        print("Planner Error:", e)

        return {
            "action": "chat",
            "message": "Sorry Boss, I couldn't understand the request."
        }