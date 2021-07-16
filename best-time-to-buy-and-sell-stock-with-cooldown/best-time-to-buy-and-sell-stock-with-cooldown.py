class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0, dp_i_1, dp_pre_0 = 0, float('-inf'), 0
        for p in prices:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, dp_pre_0 - p)
            dp_pre_0 = temp
        return dp_i_0