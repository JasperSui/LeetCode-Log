class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, window_sum, min_len = 0, 0, 0, float('inf')
        while right < len(nums):
            c = nums[right]
            right += 1
            window_sum += c
            while window_sum >= target:
                min_len = min(min_len, right-left)
                d = nums[left]
                left += 1
                window_sum -= d
        return min_len if min_len != float('inf') else 0