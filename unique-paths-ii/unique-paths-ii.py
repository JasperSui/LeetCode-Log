class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        dp = [0] * width
        dp[0] = 1
        for row in grid:
            for i in range(len(row)):
                if row[i] == 1:
                    dp[i] = 0
                elif i > 0:
                    dp[i] += dp[i-1]
        return dp[-1]
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        width = len(obstacleGrid[0])
        dp = [0] * width
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j-1]
        return dp[-1]
        
        
        
#         if not obstacleGrid: return 0
#         m, n = len(obstacleGrid[0]), len(obstacleGrid)
#         stones = {f'{x},{y}' for x, a in enumerate(obstacleGrid) for y, b in enumerate(a) if a == 1 or b == 1}
#         dp = {s: 0 for s in stones}
#         print(stones)
#         print(dp)
#         def calc(dp=dp, m=0, n=0):
#             key = f'{m},{n}'
#             if key in dp:
#                 return dp[key]
#             if m == 1 and n == 1: return 1 - dp['0,0']
#             if m == 0 or n == 0: return 0
#             dp[key] = calc(dp, m-1, n) + calc(dp, m, n-1)
#             print(dp)
#             return dp[key]
#         print(dp)
#         return calc(dp, m, n)
        