class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.dfs(s1, s2, s3, 0, 0, 0, defaultdict(lambda: -1))
    
    def dfs(self, s1, s2, s3, i, j, k, memo):
        key = f"{i},{j}"
        if key in memo:
            return memo[key] == 1

        if len(s1) + len(s2) != len(s3):
            memo[key] = 0
            return False
        
        if i == len(s1) and j == len(s2) and k == len(s3):
            memo[key] = 1
            return True
        
        if i == len(s1):
            while j < len(s2):
                if s2[j] != s3[k]:
                    memo[key] = 0
                    return False
                j += 1
                k += 1
            memo[key] = 1
            return True
        
        if j == len(s2):
            while i < len(s1):
                if s1[i] != s3[k]:
                    memo[key] = 0
                    return False
                i += 1
                k += 1
            memo[key] = 1
            return True
        
        if s1[i] == s3[k]:
            if self.dfs(s1, s2, s3, i+1, j, k+1, memo):
                memo[key] = 1
                return True
        
        if s2[j] == s3[k]:
            if self.dfs(s1, s2, s3, i, j+1, k+1, memo):
                memo[key] = 1
                return True

        memo[key] = 0
        return False
        
        