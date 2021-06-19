class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mi, ma, n = min(nums), max(nums), len(nums)
        if mi == ma: return 0
        bucketSize = math.ceil((ma - mi) / (n - 1))
        minBucket = [float('inf')] * n
        maxBucket = [float('-inf')] * n
        
        for num in nums:
            idx = (num - mi) // bucketSize
            minBucket[idx] = min(num, minBucket[idx])
            maxBucket[idx] = max(num, maxBucket[idx])
        
        maxGap = float('-inf')
        prev = mi
        for i in range(len(nums)):
            if minBucket[i] == float('inf'): continue
            maxGap = max(maxGap, minBucket[i] - prev)
            prev = maxBucket[i]
        return maxGap