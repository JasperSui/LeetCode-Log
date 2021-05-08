class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start_index = 0
        ans = 0
        for i, c in enumerate(s):
            if c in used and start_index <= used[c]:
                start_index = used[c] + 1
            else:
                ans = max(ans, i - start_index + 1)
            used[c] = i
        return ans