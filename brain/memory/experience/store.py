import json
import os


class ExperienceStore:
    """
    Stores execution experience for DON (simple log-based memory).
    """

    def __init__(self, path="brain/storage/experience.json"):
        self.path = path
        self._ensure_file()

    # -------------------------
    # INIT FILE
    # -------------------------
    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    # -------------------------
    # READ
    # -------------------------
    def _read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    # -------------------------
    # WRITE
    # -------------------------
    def _write(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    # -------------------------
    # ADD EXPERIENCE (FIXED)
    # -------------------------
    def add(self, data: dict):
        """
        Stores a single experience entry.
        Expected format:
        {
            "goal": str,
            "task": str,
            "plan": str,
            "result": str,
            "status": str,
            "reason": str (optional)
        }
        """

        items = self._read()
        items.append(data)
        self._write(items)

    # -------------------------
    # GETTERS (optional but useful)
    # -------------------------
    def get_all(self):
        return self._read()

    def get_successes(self):
        return [x for x in self._read() if x.get("status") == "success"]

    def get_failures(self):
        return [x for x in self._read() if x.get("status") == "failure"]