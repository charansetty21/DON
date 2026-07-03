import json
import os


class GoalDB:
    """
    File-based persistent storage for goals.
    """

    def __init__(self, file_path="brain/storage/goals.json"):
        self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def _read(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    # -------------------------
    # CREATE / UPDATE
    # -------------------------
    def save_goal(self, goal_id, goal_data):
        data = self._read()
        data[goal_id] = goal_data
        self._write(data)

    def update_goal(self, goal_id, updates: dict):
        data = self._read()

        if goal_id not in data:
            return

        data[goal_id].update(updates)
        self._write(data)

    # -------------------------
    # FETCH
    # -------------------------
    def get_goal(self, goal_id):
        data = self._read()
        return data.get(goal_id)

    def get_all_goals(self):
        return self._read()

    def get_active_goals(self):
        data = self._read()
        return {
            k: v for k, v in data.items()
            if v.get("status") == "active"
        }