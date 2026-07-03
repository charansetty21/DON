import brain.tools.system_tools

from brain.executor import execute_plan

plan = {
    "action": "tool",
    "tool": "current_time",
    "arguments": {}
}

print(execute_plan(plan))