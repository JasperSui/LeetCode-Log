class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_sub(nums, i, j):
            rob, not_rob = 0, 0
            for idx in range(i, j):
                num = nums[idx]
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums: return 0
        elif len(nums) == 1: return nums[0]
        else:
            return max(rob_sub(nums, 1, len(nums)), rob_sub(nums, 0, len(nums)-1))