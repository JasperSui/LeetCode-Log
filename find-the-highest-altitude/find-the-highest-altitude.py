class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = curr = 0
        for n in gain:
            curr += n
            ans = max(ans, curr)
        return ans