class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            if not grid[i][0]:
                self.dfs(grid, i, 0, m, n)
            if not grid[i][n-1]:
                self.dfs(grid, i, n-1, m, n)
                
        for j in range(n):
            if not grid[0][j]:
                self.dfs(grid, 0, j, m, n)
            if not grid[m-1][j]:
                self.dfs(grid, m-1, j, m, n)

        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    self.dfs(grid, i, j, m, n)
                    ans += 1
        return ans
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j]: return 0
        
        grid[i][j] = 1
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n)