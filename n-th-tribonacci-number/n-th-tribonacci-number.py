class Solution:
    def tribonacci(self, n: int, memo: dict = {}) -> int:
        if n == 0: return 0
        elif n in (1, 2): return 1
        elif n in memo: return memo[n]
        memo[n] = self.tribonacci(n-3, memo) + self.tribonacci(n-2, memo) + self.tribonacci(n-1, memo)
        return memo[n]