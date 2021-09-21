class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = [0] * n, [0] * m
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    col[i] += 1
                    row[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row[j] > 1 or col[i] > 1):
                    ans += 1
        return ans