class Solution:
    def longestPalindrome(self, s: str) -> str:
        # from inner to outer
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i+1), res, key=len)
        return res
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r] # because s[l] != s[r], so l have to plus 1, r have to minus 1, to meet the s[l] == s[r]
        
        