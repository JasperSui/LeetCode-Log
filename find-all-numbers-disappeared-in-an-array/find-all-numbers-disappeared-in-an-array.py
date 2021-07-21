class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(1) space
        for n in nums:
            index = abs(n) - 1
            nums[index] = - abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        
        # # O(n) space
        # return list(set(range(1, len(nums)+1)) - set(nums))