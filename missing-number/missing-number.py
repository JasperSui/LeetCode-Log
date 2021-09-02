class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(0)
        ans = 0
        for i in range(len(nums)):
            ans ^= i ^ nums[i]
        return ans