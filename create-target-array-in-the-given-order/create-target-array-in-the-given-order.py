class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = [][:]
        for i, v in enumerate(nums):
            res.insert(index[i], nums[i])
        return res