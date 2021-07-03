class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon[0])
        n = len(dungeon)
        dp = [[float('inf')] * (m+1) for _ in range(n+1)]

        dp[n][m-1] = 1
        dp[n-1][m] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                need_hp = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                if need_hp <= 0:
                    need_hp = 1
                dp[i][j] = need_hp
        
        return dp[0][0]