class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zero, one = 0, 0
            for c in s:
                if c == '0': zero += 1
                else: one += 1
            
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one] + 1) 
        return dp[m][n]
        
        
        
        
        
        
        
        
        
        
        
        
#         strs.sort(key=len, reverse=True)
#         self.ans = 0
#         self.dfs(strs, m, n, 0)
#         return self.ans
    
#     def dfs(self, strs, m, n, ans):
#         if m < 0 or n < 0:
#             return
#         s = strs.pop()
#         c = collections.Counter(s)
#         if c['0'] > m or c['1'] > n:
#             return
#         ans += 1
#         self.ans = max(self.ans, ans)
#         for i in range(len(strs)):
#             self.dfs(strs[i:], m-c['0'], n-c['1'], ans)