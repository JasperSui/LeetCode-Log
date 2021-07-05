class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_left, new_right = newInterval
        left = [[l, r] for l, r in intervals if r < new_left]
        right = [[l, r] for l, r in intervals if l > new_right]
        if left + right != intervals:
            new_left = min(new_left, intervals[len(left)][0])
            new_right = max(new_right, intervals[len(intervals)-len(right)-1][1])
        return left + [[new_left, new_right]] + right