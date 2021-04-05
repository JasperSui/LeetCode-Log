class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: return mid
            if nums[mid+1] > nums[mid]: low = mid +1
            elif nums[mid-1] > nums[mid]: high = mid
        return low