class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0]:
                self.dfs(grid, i, 0, m, n)
            if grid[i][n-1]:
                self.dfs(grid, i, n-1, m, n)
        
        for j in range(n):
            if grid[0][j]:
                self.dfs(grid, 0, j, m, n)
            if grid[m-1][j]:
                self.dfs(grid, m-1, j, m, n)
        
        return sum(grid[i][j] for i in range(m) for j in range(n))
        
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or not grid[i][j]: return
        grid[i][j] = 0
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n)