class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(set)
        for (a, b), v in zip(equations, values):
            # for example, a/b = 2.0, then b/a will be 0.5
            # so we need to do these both
            d[a].add((b, v))
            d[b].add((a, 1/v))
        
        def find(a, b):
            if not a in d and not b in d:
                return -1.0

            queue = [(a, 1.0)]
            visited = set()

            while queue:
                new_queue = []
                for front, curr_val in queue:
                    if front == b:
                        return curr_val
                    visited.add(front)
                    for neigh, value in d[front]:
                        if neigh not in visited:
                            new_queue.append((neigh, curr_val * value))
                queue = new_queue

            return -1.0
        
        return [find(x, y) for x, y in queries]