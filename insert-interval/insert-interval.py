class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_left, new_right = newInterval
        left_part = [[l, r] for [l, r] in intervals if r < new_left]
        right_part = [[l, r] for [l, r] in intervals if l > new_right]
        if left_part + right_part != intervals:
            new_left = min(new_left, intervals[len(left_part)][0])
            new_right = max(new_right, intervals[~len(right_part)][1])
        return left_part + [[new_left, new_right]] + right_part