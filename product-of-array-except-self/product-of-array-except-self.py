class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            if i > 0:
                left *= nums[i-1]
            res[i] = left
        
        for i in range(n-1, -1, -1):
            if i < n-1:
                right *= nums[i+1]
            res[i] *= right
        
        return res