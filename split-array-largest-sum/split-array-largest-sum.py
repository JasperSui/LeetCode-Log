class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lower, upper = max(nums), sum(nums)
        if len(nums) == m: return lower
        
        low, high = lower, upper
        while low < high:
            mid = low + (high - low) // 2
            if self.cut(nums, mid) > m:
                low = mid + 1
            else:
                high = mid
        return low
    
    def cut(self, nums, mid):
        total, k = 0, 1
        for n in nums:
            total += n
            if total > mid:
                total = n
                k += 1
        return k