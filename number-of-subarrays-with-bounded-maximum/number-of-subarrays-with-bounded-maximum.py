class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = cnt = 0
            for n in nums:
                if n <= bound:
                    cnt += 1
                    ans += cnt
                else:
                    cnt = 0
            return ans
        return count(right) - count(left - 1)