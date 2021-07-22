class Solution:
    def fib(self, n: int, dp={}) -> int:
        if n in (0, 1): return n
        if n in dp: return dp[n]
        res = self.fib(n-1) + self.fib(n-2)
        dp[n] = res
        return dp[n]