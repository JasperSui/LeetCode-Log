class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob_sub(l, r):
            pre2, pre1 = 0, 0
            for p in nums[l:r]:
                curr = max(pre2 + p, pre1)
                pre2, pre1 = pre1, curr
            return max(pre2, pre1)
        return max(rob_sub(0, len(nums)-1), rob_sub(1, len(nums)))