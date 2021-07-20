class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            low, high = 0, size
            while low != high:
                mid = low + (high - low) // 2
                if tails[mid] < n:
                    low = mid + 1
                else:
                    high = mid
            tails[low] = n
            size = max(size, low + 1)
        return size
            