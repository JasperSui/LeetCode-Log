class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = grid[sr][sc]
        
        m, n = len(grid), len(grid[0])
        self.dfs(grid, sr, sc, m, n, color, newColor)
        return grid
        
    def dfs(self, grid, i, j, m, n, color, new_color):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != color or grid[i][j] == new_color: return
        
        grid[i][j] = new_color
        self.dfs(grid, i+1, j, m, n, color, new_color)
        self.dfs(grid, i-1, j, m, n, color, new_color)
        self.dfs(grid, i, j+1, m, n, color, new_color)
        self.dfs(grid, i, j-1, m, n, color, new_color)
        