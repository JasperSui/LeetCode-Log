class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find smallest number first
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] > nums[high]: low = mid + 1
            else: high = mid
            print(low, high)
        small_index = low

        # Find out in which side the target lies, means narrow down the nums for what we really want
        low, high = 0, len(nums)-1
        if target >= nums[small_index] and target <= nums[high]:
            low = small_index
        else: high = small_index

        # Do normal binary search
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: high = mid - 1
            else: low = mid + 1
        return -1
        