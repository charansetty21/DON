from brain.tools.tool_registry import registry


class ChainResolver:
    """
    Detects implicit tool dependencies and expands plans.
    """

    def __init__(self):
        # simple dependency rules (v1)
        self.dependencies = {
            "save_notes": ["time", "date"],
        }

    def resolve(self, plan):
        """
        Expands plan by injecting missing dependency steps.
        """

        if plan.action != "sequence":
            return plan

        expanded_steps = []

        for step in plan.steps:

            tool_name = step.tool

            # inject dependencies if any
            if tool_name in self.dependencies:

                for dep in self.dependencies[tool_name]:
                    if registry.get(dep):
                        expanded_steps.append(
                            type(step)(
                                tool=dep,
                                arguments={}
                            )
                        )

            expanded_steps.append(step)

        plan.steps = expanded_steps
        return plan