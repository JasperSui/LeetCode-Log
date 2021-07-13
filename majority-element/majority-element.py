class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums) // 2
        for num in nums:
            d[num] += 1
            if d[num] > n: return num