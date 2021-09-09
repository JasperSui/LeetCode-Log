class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans, sums = 0, 0
        
        for n in nums:
            sums += n
            ans += d[sums - k]
            d[sums] += 1

        return ans