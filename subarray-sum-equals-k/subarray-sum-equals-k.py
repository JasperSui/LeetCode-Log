class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        sums = 0
        ans = 0
        
        for n in nums:
            sums += n
            ans += d[sums - k]
            d[sums] += 1
        
        return ans