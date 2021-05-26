class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution 1
        # return sum(range(len(nums)+1)) - sum(nums)
    
        # Solution 2
        # len_n = len(nums)
        # res = 0 ^ len_n
        # for i in range(len(nums)):
        #     res ^= i ^ nums[i]
        # return res
    
        # Solution 3
        # len_n = len(nums)
        # res = len_n
        # for i in range(len(nums)):
        #     res += i - nums[i]
        # return res
        
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res        
    