class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = (1 << n - 1) * m
        for j in range(1, n):
            curr = sum(grid[i][j] == grid[i][0] for i in range(m))
            res += max(curr, m - curr) * (1 << n - 1 - j)
        return res
        
        
#         m, n = len(grid), len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 row_1_count = sum(grid[i][y] for y in range(n))
#                 if row_1_count*2 >= n:
#                     self.flip(grid, i, j, m, n, True)
                
#                 col_1_count = sum(grid[x][j] for x in range(m))
#                 if col_1_count*2 >= m:
#                     self.flip(grid, i, j, m, n, False)
#         print(grid)
        
#     def flip(self, grid, i, j, m, n, is_row):
#         if is_row:
#             for y in range(n):
#                 grid[i][y] = 1 if grid[i][y] == 0 else 1
#         else:
#             for x in range(m):
#                 grid[x][j] = 1 if grid[x][j] == 0 else 1