class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [[0,0,0]] + sorted(map(sorted, cuboids))
        dp = [0] * len(cuboids)
        for j in range(1, len(cuboids)):
            for i in range(j):
                if all(cuboids[i][k] <= cuboids[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + cuboids[j][2])
        return max(dp)