class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        return (first - 1) * (second - 1)