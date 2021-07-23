class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        l, r = 0, len(nums)-1
        
        while l < len(nums) - 1 and nums[l] <= nums[l+1]:
            l += 1
        
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        if l > r: return 0
        
        temp = nums[l:r+1]
        temp_min = min(temp)
        temp_max = max(temp)
        
        while l > 0 and temp_min < nums[l-1]:
            l -= 1
        
        while r < len(nums) - 1 and temp_max > nums[r+1]:
            r += 1
        
        return r - l + 1