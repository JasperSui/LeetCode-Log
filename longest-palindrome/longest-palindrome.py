class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        single = False
        ans = 0
        for v in d.values():
            ans += v
            if v % 2 == 1:
                ans -= 1
                single = True
        return ans + single