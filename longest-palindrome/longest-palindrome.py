class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)
        ans = 0
        single = False
        for v in d.values():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
                single = True
        return ans + 1 if single else ans