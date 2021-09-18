class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        local_max, ans = nums[0], 0
        m = local_max
        for i in range(1, len(nums)):
            if local_max > nums[i]:
                local_max = m
                ans = i
            else:
                m = max(m, nums[i])
        return ans + 1