class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, ans, curr_sum = 0, 0, float('inf'), 0
        while right < len(nums):
            curr_sum += nums[right]
            right += 1
            while curr_sum >= target:
                ans = min(ans, right-left)
                curr_sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0