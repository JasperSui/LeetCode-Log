class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            self.dfs(grid, i, 0, m, n)
            self.dfs(grid, i, n-1, m, n)
        
        for i in range(n):
            self.dfs(grid, 0, i, m, n)
            self.dfs(grid, m-1, i, m, n)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += 1
        return ans
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or not grid[i][j]: return
        grid[i][j] = 0
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n)