from brain.goal.controller import GoalController
from brain.memory.memory import memory
import brain.tools

controller = GoalController()

def run_don(user_input: str):

    memory.basic.add_short(f"User: {user_input}")
    memory.rag.add(user_input)

    result = controller.run(user_input)

    memory.basic.add_short(f"DON: {result}")

    return result