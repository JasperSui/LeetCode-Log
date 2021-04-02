class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 0: return 0
        # elif n == 1: return 1
        # elif n == 2: return 1
        # else:
        #     return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a+b+c
        return a