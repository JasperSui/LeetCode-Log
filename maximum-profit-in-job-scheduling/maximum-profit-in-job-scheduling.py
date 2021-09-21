class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            index = bisect.bisect(dp, [s+1]) - 1
            if dp[index][1] + p > dp[-1][1]:
                dp.append([e, dp[index][1] + p])
        return dp[-1][1]