class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] < 0:
                    ans += m - j
                    break
        return ans
            