class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        dp[0] = 1
        return self.helper(nums, target, dp)
    
    def helper(self, nums, target, dp):
        if dp[target] != -1: return dp[target]
        
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.helper(nums, target-nums[i], dp)
        dp[target] = res
        return res