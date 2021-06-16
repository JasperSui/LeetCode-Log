class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        _grid = list(zip(*grid))
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = min(max(grid[i]), max(_grid[j]))
                if temp > grid[i][j]:
                    ans += temp - grid[i][j]
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(grid)
#         tb = [0] * n
#         lr = [0] * n
#         ans = 0
#         for i in range(n):
#             for j in range(n):
#                 tb[i] = max(tb[i], grid[i][j])
#                 lr[i] = max(lr[i], grid[j][i])
                
#         for i in range(n):
#             for j in range(n):
#                 ans += min(tb[i], lr[j]) - grid[i][j]
#         return ans
            