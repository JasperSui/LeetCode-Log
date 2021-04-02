class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = {}
        for n in arr:
            count[n] = 1 + count.get(n - difference, 0)
        return max(count.values())