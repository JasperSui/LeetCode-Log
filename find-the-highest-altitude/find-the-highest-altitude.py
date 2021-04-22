class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = t = 0
        gain = [0] + gain
        for g in gain:
            t += g
            s = max(s, t)
        return s