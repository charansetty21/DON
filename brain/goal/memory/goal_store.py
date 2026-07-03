import uuid
from brain.storage.goal_db import GoalDB


db = GoalDB()


class GoalStore:

    def create_goal(self, user_input, tasks):
        goal_id = str(uuid.uuid4())

        goal = {
            "id": goal_id,
            "original_input": user_input,
            "tasks": tasks,
            "completed": [],
            "pending": tasks.copy(),
            "status": "active"
        }

        db.save_goal(goal_id, goal)

        return goal_id

    def mark_completed(self, goal_id, task, result):

        goal = db.get_goal(goal_id)

        if not goal:
            return

        if task in goal["pending"]:
            goal["pending"].remove(task)

        goal["completed"].append({
            "task": task,
            "result": result
        })

        if not goal["pending"]:
            goal["status"] = "completed"

        db.update_goal(goal_id, goal)

    def get_goal(self, goal_id):
        return db.get_goal(goal_id)

    def get_active_goals(self):
        return db.get_active_goals()