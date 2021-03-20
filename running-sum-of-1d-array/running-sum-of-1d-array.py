class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(1)
        r = 0
        res = []
        for n in nums:
            res.append(n+r)
            r += n
        return res