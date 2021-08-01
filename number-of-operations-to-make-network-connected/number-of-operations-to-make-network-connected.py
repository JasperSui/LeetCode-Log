class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1

        graph = [set() for _ in range(n)]
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        
        visited = [0] * n
        
        def dfs(i):
            if visited[i]: return 0
            visited[i] = 1
            for j in graph[i]:
                dfs(j)
            return 1
        
        res = -1
        for i in range(n):
            res += dfs(i)
        return res