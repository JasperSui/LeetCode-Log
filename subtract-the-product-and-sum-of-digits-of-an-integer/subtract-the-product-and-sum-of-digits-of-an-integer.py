class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for i in map(int, list(str(n))):
            p *= i
            s += i
        return p - s