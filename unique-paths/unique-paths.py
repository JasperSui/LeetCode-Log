class Solution:
    def uniquePaths(self, m: int, n: int, dp={}) -> int:
        # Time: O(mn)
        # Space: O(m+n)
        if f'{m},{n}' in dp: return dp[f'{m},{n}']
        if m == 1 and n == 1: return 1
        if m == 0 or n == 0: return 0
        dp[f'{m},{n}'] = self.uniquePaths(m-1, n, dp) + self.uniquePaths(m, n-1, dp)
        return dp[f'{m},{n}']
        
        # aux = [[1 for i in range(n)] for i in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         aux[i][j] = aux[i][j-1] + aux[i-1][j]
        # return aux[-1][-1]
    