class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            if d[n] > len(nums) // 2: return n
        return max(d.items(), key=lambda x: x[1])[0]