from brain.goal.decomposer import decompose_goal
from brain.goal.memory.goal_memory import goal_memory
from brain.planner.planner import build_plan
from brain.executor import execute_plan
from brain.memory.experience.store import ExperienceStore


class GoalController:

    def __init__(self):
        self.experience = ExperienceStore()

    def run(self, user_input: str):

        # Step 1: Decompose the goal
        tasks = decompose_goal(user_input)
        print(f"[Controller] Tasks → {tasks}")

        # Step 2: Create goal
        goal_id = goal_memory.create_goal(user_input, tasks)

        results = []

        # Step 3: Execute each task once
        for task in tasks:

            print(f"\n[Task] {task}")

            plan = build_plan(task)
            print(f"[Plan] {plan}")

            result = execute_plan(plan)
            print(f"[Result] {result}")

            self.experience.add({
                "goal": user_input,
                "task": task,
                "plan": str(plan),
                "result": str(result),
                "status": "completed",
                "reason": ""
            })

            goal_memory.mark_completed(goal_id, task, result)
            results.append(result)

        return {
            "goal_id": goal_id,
            "results": results
        }