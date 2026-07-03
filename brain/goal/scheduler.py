from brain.goal.memory.goal_memory import goal_memory


class GoalScheduler:
    """
    Picks the next best task across all active goals.
    """

    def score_goal(self, goal):

        score = 0

        # 1. unfinished work increases priority
        score += len(goal.get("pending", [])) * 2

        # 2. older goals get higher priority (simplified)
        score += 1

        # 3. urgency detection (simple keyword heuristic)
        text = goal.get("original_input", "").lower()

        if "urgent" in text or "now" in text:
            score += 10

        if "important" in text:
            score += 5

        # 4. near completion bonus
        if len(goal.get("pending", [])) == 1:
            score += 3

        return score

    def get_next_task(self):

        active_goals = goal_memory.get_active_goals()

        if not active_goals:
            return None, None

        best_goal = None
        best_score = -1

        # -------------------------
        # FIND BEST GOAL
        # -------------------------
        for goal in active_goals.values():

            score = self.score_goal(goal)

            if score > best_score:
                best_score = score
                best_goal = goal

        if not best_goal:
            return None, None

        # -------------------------
        # PICK NEXT TASK
        # -------------------------
        if not best_goal.get("pending"):
            return None, None

        next_task = best_goal["pending"][0]

        return best_goal["id"], next_task