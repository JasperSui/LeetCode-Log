class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for n in arr:
            count = 1
            if n-difference in d:
                count = d[n-difference] + 1
            d[n] = count
        return max(d.values())
        