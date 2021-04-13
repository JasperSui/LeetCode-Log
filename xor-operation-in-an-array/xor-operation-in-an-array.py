class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = [start + 2*x for x in range(n)]
        ans = 0
        for i in result:
            ans = ans ^ i
        return ans