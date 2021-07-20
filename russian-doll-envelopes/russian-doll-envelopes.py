class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums, res = [j for _, j in envelopes], []
        for curr in nums:
            index = bisect.bisect_left(res, curr)
            res[index:index+1] = [curr]
        return len(res)