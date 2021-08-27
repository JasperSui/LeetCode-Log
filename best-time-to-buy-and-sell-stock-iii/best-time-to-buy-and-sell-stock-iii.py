class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_1_0, dp_i_1_1 = 0, float('-inf') # First transaction
        dp_i_2_0, dp_i_2_1 = 0, float('-inf') # Second transaction
        for p in prices:
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + p)
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - p)
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + p)
            dp_i_1_1 = max(dp_i_1_1, - p)
        return dp_i_2_0