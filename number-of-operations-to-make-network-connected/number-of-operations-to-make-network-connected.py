class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        graph = [set() for _ in range(n)]
        for x, y in connections:
            graph[x].add(y)
            graph[y].add(x)
        
        visited = [0] * n
        
        def dfs(i):
            if visited[i]: return 0
            visited[i] = 1
            for j in graph[i]:
                dfs(j)
            return 1
        
        connected = 0
        for i in range(n):
            connected += dfs(i)
        return connected - 1
        