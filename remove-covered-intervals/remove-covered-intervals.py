class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        stack = []
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for s, e in intervals:
            if stack and s >= stack[-1][0] and e <= stack[-1][1]: continue
            stack.append([s, e])
        return len(stack)