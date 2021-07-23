class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = 0
        visited = set()

        def dfs(node):
            for neigh, adj in enumerate(isConnected[node]):
                if adj and neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)

        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans