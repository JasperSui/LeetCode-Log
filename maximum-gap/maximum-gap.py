class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mi, ma, n = min(nums), max(nums), len(nums)
        if mi == ma: return 0
        bucket_size = math.ceil((ma - mi) / (n - 1))
        min_buckets = [float('inf')] * n
        max_buckets = [float('-inf')] * n
        
        for n in nums:
            idx = (n - mi) // bucket_size
            min_buckets[idx] = min(min_buckets[idx], n)
            max_buckets[idx] = max(max_buckets[idx], n)
        
        max_gap = float('-inf')
        prev = mi
        for i in range(len(nums)):
            if min_buckets[i] == float('inf'): continue
            max_gap = max(max_gap, min_buckets[i] - prev)
            prev = max_buckets[i]
        return max_gap