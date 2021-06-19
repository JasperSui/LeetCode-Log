class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        prev = float('-inf')
        points.sort(key=lambda x: x[1])
        for start, end in points:
            if prev >= start: continue
            ans += 1
            prev = end
        return ans