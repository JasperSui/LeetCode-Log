class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = {}
        for n in arr:
            res[n] = res.get(n-difference, 0) + 1
        return max(res.values())