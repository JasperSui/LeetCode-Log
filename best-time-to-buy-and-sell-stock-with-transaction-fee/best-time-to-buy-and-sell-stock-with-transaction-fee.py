class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0