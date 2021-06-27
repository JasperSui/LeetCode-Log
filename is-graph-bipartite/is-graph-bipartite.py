class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(node):
            for i in graph[node]:
                if i in color:
                    if color[i] == color[node]:
                        return False
                else:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True