class Solution:
    def fib(self, n: int) -> int:
        d = {}
        if n in d: return d[n]
        if n == 0 or n == 1: return n
        d[n] = self.fib(n-1) + self.fib(n-2)
        return d[n]