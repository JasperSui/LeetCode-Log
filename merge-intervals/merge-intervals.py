class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        curr = 0
        intervals.sort(key=lambda x: x[0])
        while curr < len(intervals)-1:
            curr_1, curr_2 = intervals[curr]
            next_1, next_2 = intervals[curr+1]
            if curr_2 >= next_1:
                intervals[curr] = [min(curr_1, next_1), max(curr_2, next_2)]
                del intervals[curr+1]
            else:
                curr += 1
        return intervals