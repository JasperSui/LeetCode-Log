class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = _max = _min = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                _max, _min = _min, _max
            
            _max = max(nums[i], nums[i] * _max)
            _min = min(nums[i], nums[i] * _min)
            
            res = max(res, _max)
        return res