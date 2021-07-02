class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0: return
        elif target == 0:
            res.append(path)
            return
        else:
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)