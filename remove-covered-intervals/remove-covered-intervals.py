class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for s, e in intervals:
            if stack and stack[-1][0] <= s and stack[-1][1] >= e:
                continue
            stack.append([s,e])
        return len(stack)