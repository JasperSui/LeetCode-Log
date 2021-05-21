class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            while nums[low] > nums[mid]: 
                low += 1
            if nums[mid] > nums[high]: low = mid + 1
            elif nums[mid] < nums[high]: high = mid
        return nums[low]