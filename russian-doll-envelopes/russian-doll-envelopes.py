class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [None] * len(envelopes)
        size = 0
        for s, e in envelopes:
            low, high = 0, size
            while low < high:
                mid = low + (high - low) // 2
                if dp[mid] < e: low = mid + 1
                else: high = mid
            dp[low] = e
            if low == size:
                size += 1
        return size