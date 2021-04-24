class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2
        
        # buy = []
        
        # dp_i_1_0, dp_i_1_1 = 0, float('-inf')
        # dp_i_2_0, dp_i_2_1 = 0, float('-inf')
        # for p in prices:
        #     dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + p)
        #     dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - p)
        #     dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + p)
        #     dp_i_1_1 = max(dp_i_1_1, -p)
        # return dp_i_2_0
        
        