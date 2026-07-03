from brain.planner.planner import build_plan
from brain.reflection.judge import judge


class ReflectionEngine:

    def reflect(self, user_input, result):

        evaluation = judge(user_input, result)

        print(f"[Reflection] Judge → {evaluation}")

        if evaluation["status"] == "success":
            return None

        print("[Reflection] Failure detected → re-planning")

        # regenerate plan using same input
        new_plan = build_plan(user_input)

        return new_plan