class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]*i for i in range(1, numRows+1)]
        if numRows <= 2: return dp[:numRows]
        for i in range(2, numRows):
            for j in range(i+1):
                if not (j == 0 or j == i):
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp