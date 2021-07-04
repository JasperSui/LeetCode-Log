class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        
        m = len(matrix[0])
        n = len(matrix)
        
        dp = [[0]* (m+1) for _ in range(n+1)]
        max_side = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
        return max_side ** 2
        