class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            self.dfs(grid, i, 0, m, n, 1)
            self.dfs(grid, i, n-1, m, n, 1)
        
        for i in range(n):
            self.dfs(grid, 0, i, m, n, 1)
            self.dfs(grid, m-1, i, m, n, 1)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    self.dfs(grid, i, j, m, n, 1)
                    ans += 1
        return ans
        
        
    def dfs(self, grid, i, j, m, n, target):
        curr = abs(target - 1)
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != curr or grid[i][j] == target: return
        grid[i][j] = target
        
        self.dfs(grid, i-1, j, m, n, target)
        self.dfs(grid, i+1, j, m, n, target)
        self.dfs(grid, i, j-1, m, n, target)
        self.dfs(grid, i, j+1, m, n, target)