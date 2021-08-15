class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr: return 0
        ans = ma = 0
        for i in range(len(arr)):
            ma = max(ma, arr[i])
            if ma == i:
                ans += 1
        return ans