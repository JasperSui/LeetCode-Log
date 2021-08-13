class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            low, high = s.find(c), s.rfind(c)
            if low > -1:
                res += len(set(s[low+1:high]))
        return res