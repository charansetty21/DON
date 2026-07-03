from brain.executor import execute_plan

plan = {
    "action": "tool",
    "tool": "time"
}

print(execute_plan(plan))