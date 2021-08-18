class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [0, 0]
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                start = end = mid
                while start > 0 and nums[start-1] == nums[mid]:
                    start -= 1
                while end < len(nums)-1 and nums[end+1] == nums[mid]:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                low = mid + 1
            else: high = mid - 1
        return [-1, -1]