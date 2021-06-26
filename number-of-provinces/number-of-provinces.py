class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(node):
            for neigh, adj in enumerate(isConnected[node]):
                if adj and neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
        
        
        
        
        
        
        
        
        
#         graph = []
#         visited = set()
#         ans = 0
        
#         for i, node in enumerate(isConnected):
#             s = set()
#             for j, x in enumerate(node):
#                 if i == j: continue
#                 if x == 1: s.add(j)
#             graph.append(s)
        
#         for i in range(isConnected):
#             if not graph[i]: ans += 1
#             queue = [graph[i]]
            
            
            