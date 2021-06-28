class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        curr = 0
        for c in s:
            if c == '(':
                curr += 1
            elif c == ')':
                curr -= 1
            ans = max(ans, curr)
        return ans