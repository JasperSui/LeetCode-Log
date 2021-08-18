class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]: low = mid + 1
            else: high = mid
        small_index = low
        
        low, high = 0, len(nums)-1
        if nums[small_index] <= target <= nums[high]:
            low = small_index
        else:
            high = small_index
        
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1
        return -1