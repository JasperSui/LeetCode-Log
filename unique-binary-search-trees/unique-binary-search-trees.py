class Solution:
    def numTrees(self, n: int) -> int:
        return self.calc(1, n, {})
    
    def calc(self, start, end, dp):
        if start > end: return 1
        curr = f"{start},{end}"
        if curr in dp: return dp[curr]
        total = 0
        for i in range(start, end+1):
            total += self.calc(start, i-1, dp) * self.calc(i+1, end, dp)
        dp[curr] = total
        return dp[curr]