class Solution:
    def rob(self, nums: List[int]) -> int:
        last = now = 0
        for i in nums:
            print(last, now, i)
            last, now = now, max(last+i, now)
        return now