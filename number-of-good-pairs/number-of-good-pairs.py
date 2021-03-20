class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = defaultdict(int)
        num = 0
        for i in nums:
            if i in res:
                num += res[i]
            res[i] += 1
        return num