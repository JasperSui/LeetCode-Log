class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        color = [0 for _ in range(n+1)]
        
        for x, y in dislikes:
            graph[x].add(y)
            graph[y].add(x)
        
        def dfs(node, c):
            color[node] = c
            
            for other in graph[node]:
                if color[other] == c:
                    return False
                
                if color[other] == 0 and not dfs(other, -c):
                    return False
            return True
        
        for i in range(1, n+1):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True
        