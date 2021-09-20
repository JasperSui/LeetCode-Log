class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r = ans = 0
        for c in s:
            if c == "R":
                r += 1
            else:
                l += 1
            if l == r:
                l = r = 0
                ans += 1
        return ans