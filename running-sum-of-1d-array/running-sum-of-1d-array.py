class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        res = []
        for n in nums:
            curr += n
            res.append(curr)
        return res