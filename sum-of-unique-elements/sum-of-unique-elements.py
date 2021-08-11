class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        return sum(k for k, v in d.items() if v == 1)