from brain.memory.experience.store import ExperienceStore


store = ExperienceStore()


class ExperienceLearner:
    """
    Learns patterns from past executions.
    """

    def learn_from_result(self, goal, task, plan, result, evaluation):

        status = evaluation.get("status", "failure")
        reason = evaluation.get("reason", "")

        store.add(
            goal=goal,
            task=task,
            plan=plan,
            result=result,
            status=status,
            reason=reason
        )

    def get_success_patterns(self):
        return store.get_successes()

    def get_failure_patterns(self):
        return store.get_failures()