class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)
        
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[i], c))
            
            left.add(s[i])
        return len(res)
        
        
#         brute force
#         res = set()
#         memo = set()
#         self.dfs(s, "", res, memo)
#         return len(res)
    
#     def dfs(self, s, path, res, memo):
#         for i in range(len(s)-2):
#             if s[i] in memo: continue
#             memo.add(s[i])
#             for j in range(i+1, len(s)-1):
#                 for k in range(j+1, len(s)):
#                     path = s[i]+s[j]+s[k]
#                     if path == path[::-1]:
#                         res.add(path)