class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        dp[0] = 1
        return self.helper(nums, target, dp)
    
    def helper(self, nums, target, dp):
        if dp[target] != -1:
            return dp[target]
        
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.helper(nums, target-nums[i], dp)
        dp[target] = res
        return res
        
#         res = set()
#         visited = set()
#         self.dfs(nums, '', target, res, visited)
#         return len(res)
    
#     def dfs(self, nums, path, target, res, visited):
#         if path in visited:
#             return
#         visited.add(path)
#         if target < 0:
#             return
#         elif target == 0:
#             res.add(path)
#             return
#         for n in nums:
#             self.dfs(nums, path + str(n), target - n, res, visited)