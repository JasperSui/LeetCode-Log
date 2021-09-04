class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        size = 0
        for n in nums:
            low, high = 0, size
            while low < high:
                mid = low + (high - low) // 2
                if dp[mid] < n: low = mid + 1
                else: high = mid
            dp[low] = n
            if low == size:
                size += 1
        return size