class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False for _ in range(len(nums))]
        self.dfs(nums, [], used, res)
        return res
    
    def dfs(self, nums, path, used, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]: continue
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]: continue
            used[i] = True
            path.append(nums[i])
            self.dfs(nums, path, used, res)
            used[i] = False
            path.pop()
        