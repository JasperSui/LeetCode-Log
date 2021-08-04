class Solution:
    def tribonacci(self, n: int, dp={}) -> int:
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        if n in dp: return dp[n]
        dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return dp[n]