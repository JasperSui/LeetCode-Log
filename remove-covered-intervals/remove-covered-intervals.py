class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        stack = []
        for start, end in sorted(intervals, key=lambda x:(x[0], -x[1])):
            if stack and start >= stack[-1][0] and end <= stack[-1][1]:
                continue
            stack.append([start, end])
        return len(stack)