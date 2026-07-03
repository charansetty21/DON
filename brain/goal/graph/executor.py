from collections import defaultdict, deque
from brain.planner.planner import build_plan
from brain.executor import execute_plan
from brain.reflection.judge import judge


class GraphExecutor:

    def topological_sort(self, tasks):

        graph = defaultdict(list)
        indegree = defaultdict(int)
        task_map = {}

        # build graph
        for task in tasks:
            name = task["name"]
            task_map[name] = task

            for dep in task["depends_on"]:
                graph[dep].append(name)
                indegree[name] += 1

        queue = deque([t["name"] for t in tasks if indegree[t["name"]] == 0])

        order = []

        while queue:

            node = queue.popleft()
            order.append(node)

            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        return order, task_map

    def execute(self, tasks):

        order, task_map = self.topological_sort(tasks)

        results = {}

        for task_name in order:

            task = task_map[task_name]

            print(f"\n[Graph] Executing → {task_name}")

            plan = build_plan(task_name)

            result = execute_plan(plan)

            evaluation = judge(task_name, result)

            if evaluation["status"] != "success":
                print(f"[Graph] Task failed → {task_name}")
                continue

            results[task_name] = result

        return results