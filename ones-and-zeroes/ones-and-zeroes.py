class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for word in strs:
            num_zero, num_one = 0, 0
            for c in word:
                if c == "1":
                    num_one += 1
                else: num_zero += 1
            
            for i in range(m, num_zero-1, -1):
                for j in range(n, num_one-1, -1):
                    memo[i][j] = max(memo[i][j], memo[i - num_zero][j - num_one] + 1)
        return memo[-1][-1]
                    