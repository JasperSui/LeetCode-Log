class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        for i in range(len(nums)):
            if farest < i: return False
            farest = max(farest, i + nums[i])
        return True