class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = self.rob_sub(nums[:len(nums)-1]), self.rob_sub(nums[1:])
        return max(left, right)
        
        
    def rob_sub(self, nums):
        pre2 = pre1 = 0
        for i in range(len(nums)):
            curr = max(pre2 + nums[i], pre1)
            pre2, pre1 = pre1, curr
        return max(pre2, pre1)