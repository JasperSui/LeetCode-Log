class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums)-1
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low