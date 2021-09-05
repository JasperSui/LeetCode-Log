class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        for (x, y), v in zip(equations, values):
            graph[x].add((y, v))
            graph[y].add((x, 1/v))
        
        def find(a, b):
            if a not in graph or b not in graph:
                return -1.0
            
            queue = [(a, 1.0)]
            visited = set()
            while queue:
                new_queue = []
                for char, last_value in queue:
                    visited.add(char)
                    if char == b:
                        return last_value
                    
                    for neigh, value in graph[char]:
                        if neigh not in visited:
                            new_queue.append((neigh, last_value * value))
                queue = new_queue
            return -1
        return [find(x, y) for x, y in queries]