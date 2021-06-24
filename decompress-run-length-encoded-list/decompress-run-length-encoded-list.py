class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            times, num = nums[i:i+2]
            res += [num]*times
        return res
            