class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        for c in str(n):
            c = int(c)
            p *= c
            s += c
        return p-s