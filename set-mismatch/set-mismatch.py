class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        
        dup = -1
        
        # dup
        for n in nums:
            if nums[abs(n)-1] < 0: dup = abs(n)
            else: nums[abs(n)-1] *= -1
        
        # missing
        for i in range(len(nums)):
            if nums[i] > 0: return [dup, i + 1]
        