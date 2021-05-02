class Solution:
    def fib(self, N: int, dp={}) -> int:
        if N in dp: return dp[N]
        if N in (0, 1): return N
        dp[N] = self.fib(N-1, dp) + self.fib(N-2, dp)
        return dp[N]