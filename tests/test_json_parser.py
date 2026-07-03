from brain.json_parser import parse_plan

response = """
{
    "action": "tool",
    "tool": "current_time",
    "arguments": {}
}
"""

plan = parse_plan(response)

print(plan)