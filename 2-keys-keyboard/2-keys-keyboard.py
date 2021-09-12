class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        for i in range(2, n+1):
            while n % i == 0:
                res += i
                n /= i
        return res