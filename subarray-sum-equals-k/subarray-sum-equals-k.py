class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        d[0] = 1
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            ans += d[running_sum - k]
            d[running_sum] += 1
        return ans
        