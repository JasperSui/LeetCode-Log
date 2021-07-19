class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(set)
        for (x, y), v in zip(equations, values):
            d[x].add((y, v))
            d[y].add((x, 1/v))
        
        def find(a, b):
            if a not in d or b not in d:
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
                            new_queue.append((neigh, value * curr_val))
                queue = new_queue
            return -1.0
        
        return [find(x, y) for x, y in queries]
            