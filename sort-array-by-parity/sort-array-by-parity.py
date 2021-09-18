class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums)-1
        while low <= high:
            if nums[low] % 2 == 0:
                low += 1
            else:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
        return nums
            