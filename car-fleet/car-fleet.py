class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        ans = curr = 0
        for t in time[::-1]:
            if t > curr:
                ans += 1
                curr = t
        return ans