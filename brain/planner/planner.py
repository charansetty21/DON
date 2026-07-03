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

Available tools:

{tool_list}

Rules:

- NEVER use "output".
- NEVER use "result".
- NEVER use "notes".
- NEVER create your own schema.
- ONLY use action "chat" or "tool".
- If a tool is needed, the tool name MUST be one of the available tools.
- Return ONLY JSON.
- Do not wrap the JSON in markdown.
- Do not explain anything.

User request:
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