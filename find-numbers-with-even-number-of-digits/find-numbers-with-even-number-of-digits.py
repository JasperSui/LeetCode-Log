class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += 1 if len(str(num)) % 2 == 0 else 0
        return ans