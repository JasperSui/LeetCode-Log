class Solution:
    def rob(self, nums: List[int]) -> int:
        pre2, pre1 = 0, 0
        for i in range(len(nums)):
            curr = max(pre2 + nums[i], pre1)
            pre2, pre1 = pre1, curr
        return max(pre2, pre1)