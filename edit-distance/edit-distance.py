class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # recursion -> memo -> dp
        # if not word1 and not word2: return 0
        # if not word1: return len(word2)
        # if not word2: return len(word1)
        # if word1[0] == word2[0]:
        #     return self.minDistance(word1[1:], word2[1:])
        # insert = 1 + self.minDistance(word1, word2[1:])
        # delete = 1 + self.minDistance(word1[1:], word2)
        # replace = 1 + self.minDistance(word1[1:], word2[1:])
        # return min(insert, delete, replace)
        
        # dp
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # First col (0 = word2 empty, so the value will be word1)
        for i in range(m+1):
            dp[i][0] = i
        
        # First row (0 = word1 empty, so the value will be word2)
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[-1][-1]