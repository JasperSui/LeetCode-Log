class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(temp, start):
            self.res.append(temp.copy())
            for i in range(start, len(nums)):
                backtrack(temp + [nums[i]], i + 1)
        backtrack([], 0)
        return self.res
    
    