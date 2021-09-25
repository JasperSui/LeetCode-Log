class Solution:
    def maxDepth(self, s: str) -> int:
        opened = 0
        ans = 0
        for c in s:
            if c == "(": opened += 1
            elif c == ")": opened -= 1
            ans = max(ans, opened)
        return ans