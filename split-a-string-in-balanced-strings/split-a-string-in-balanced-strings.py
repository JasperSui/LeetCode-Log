class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = ans = 0
        for c in s:
            if c == 'R': r += 1
            else: l += 1
            if r == l:
                ans += 1
                r = l = 0
        return ans