class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n+1)
        for x, y in requests:
            count[x] += 1
            count[y+1] -= 1
        
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        ans = 0
        for val, c in zip(sorted(count[:-1]), sorted(nums)):
            ans += val * c
        
        return ans % (10 ** 9 + 7)