class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        prev = float('-inf')
        points.sort(key=lambda x: x[1])
        for s, e in points:
            if prev >= s: continue
            prev = e
            ans += 1
        return ans