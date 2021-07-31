class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j, m, n))
        return ans
        
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1: return 0
        grid[i][j] = -1
        return self.dfs(grid, i+1, j, m, n) + \
               self.dfs(grid, i-1, j, m, n) + \
               self.dfs(grid, i, j+1, m, n) + \
               self.dfs(grid, i, j-1, m, n) + 1