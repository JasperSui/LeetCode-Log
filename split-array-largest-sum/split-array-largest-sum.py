class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lower, upper = float('-inf'), 0
        for n in nums:
            lower = max(lower, n)
            upper += n
        
        if k == len(nums): return lower
        
        low, high = lower, upper + 1
        while low < high:
            mid = low + (high - low) // 2
            if self.cut_func(nums, mid) > k:
                low = mid + 1
            else:
                high = mid 
        return low
    
    def cut_func(self, nums, mid):
        total, k = 0, 1
        for n in nums:
            total += n
            if total > mid:
                total = n
                k += 1
        return k