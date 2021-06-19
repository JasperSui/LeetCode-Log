class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        print(sorted(zip(position, speed)))
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        print(time)
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res