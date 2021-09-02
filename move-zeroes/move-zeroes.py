class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_index = 0
        for n in nums:
            if n != 0:
                nums[insert_index] = n
                insert_index += 1
        
        while insert_index < len(nums):
            nums[insert_index] = 0
            insert_index += 1