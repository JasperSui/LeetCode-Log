class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], res)
        
        
        # self.res = []
        # def backtrace(temp, start):
        #     self.res.append(temp.copy())
        #     for i in range(start, len(nums)):
        #         backtrace(temp + [nums[i]], i+1)
        # backtrace([], 0)
        # return self.res
        
        
        
        
#         self.res = []
#         def backtrack(temp, start):
#             self.res.append(temp.copy())
#             for i in range(start, len(nums)):
#                 backtrack(temp + [nums[i]], i + 1)
#         backtrack([], 0)
#         return self.res
    
    