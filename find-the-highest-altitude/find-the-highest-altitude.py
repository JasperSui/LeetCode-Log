class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        ans = 0
        for a in gain:
            ans = max(ans, res[-1]+a)
            res.append(res[-1]+a)
        return ans