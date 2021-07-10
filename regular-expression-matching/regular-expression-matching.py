class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)] 
        dp[0][0] = True
        
        for j in range(2, n+1, 2):
            if p[j-1] == "*" and dp[0][j-2]:
                dp[0][j] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                curS = s[i-1]
                curP = p[j-1]
                if curS == curP or curP == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif curP == "*":
                    preCurP = p[j-2]
                    if preCurP != "." and preCurP != curS:
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
        return dp[m][n]
                
        
#         if not p: return not s
        
#         first_match = s and s[0] == p[0] or p[0] == "."
#         if len(p) >= 2 and p[1] == "*":
#             return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
#         else:
#             return s and first_match and self.isMatch(s[1:], p[1:])