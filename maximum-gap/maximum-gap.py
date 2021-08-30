class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ma, mi, n = max(nums), min(nums), len(nums)
        if ma == mi: return 0
        bucket_size = math.ceil((ma - mi) / (n - 1))
        min_buckets = [float('inf')] * n
        max_buckets = [float('-inf')] * n
        
        for n in nums:
            index = (n - mi) // bucket_size
            min_buckets[index] = min(min_buckets[index], n)
            max_buckets[index] = max(max_buckets[index], n)
        
        max_gap = float('-inf')
        prev = mi
        for i in range(len(nums)):
            if min_buckets[i] == float('inf'): continue
            max_gap = max(max_gap, min_buckets[i] - prev)
            prev = max_buckets[i]
        return max_gap
        
        