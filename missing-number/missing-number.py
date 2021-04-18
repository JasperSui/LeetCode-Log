class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution 1
        return sum(range(len(nums)+1)) - sum(nums)
    
        # Solution 2
        len_n = len(nums)
        res = 0 ^ len_n
        for n in nums:
            res ^= n
        return res