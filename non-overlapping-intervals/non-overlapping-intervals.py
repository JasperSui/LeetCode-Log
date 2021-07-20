class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        ans = 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                ans += 1
        return ans