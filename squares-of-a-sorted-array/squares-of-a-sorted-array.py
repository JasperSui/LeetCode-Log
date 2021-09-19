class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q = deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                q.appendleft(nums[l] ** 2)
                l += 1
            else:
                q.appendleft(nums[r] ** 2)
                r -= 1
        return q