class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # is_same = [a == b for a, b in zip(nums, sorted(nums))]
        # return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
        
        if len(nums) < 2: return 0
        l, r = 0, len(nums)-1
        
        while l < len(nums)-1 and nums[l] <= nums[l+1]:
            l+= 1
        
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        if l > r: return 0
        
        temp_nums = nums[l:r+1]
        temp_min = min(temp_nums)
        temp_max = max(temp_nums)
        
        while l > 0 and temp_min < nums[l-1]:
            l -= 1
        
        while r < len(nums) -1 and temp_max > nums[r+1]:
            r += 1
        
        return r - l + 1