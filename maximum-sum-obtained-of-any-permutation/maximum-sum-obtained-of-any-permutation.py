class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n+1)
        for i, j in requests:
            count[i] += 1
            count[j+1] -= 1 # represents the end of request
        
        for i in range(1, n):
            count[i] += count[i-1] # it's the frequency of index
        
        ans = 0
        for v, c in zip(sorted(count[:-1]), sorted(nums)):
            ans += v*c
        return ans % (10 ** 9 + 7)