class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0, dp_i_1 = 0, float('-inf')
        dp_pre_0 = 0
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0