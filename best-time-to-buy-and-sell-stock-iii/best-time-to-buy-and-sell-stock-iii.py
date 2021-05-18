class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy1, buy2 = float('-inf'), float('-inf')
        # sell1, sell2 = 0, 0
        # for p in prices:
        #     buy1 = max(buy1, -p)
        #     sell1 = max(sell1, buy1 + p)
        #     buy2 = max(buy2, sell1 - p)
        #     sell2 = max(sell2, buy2 + p)
        # return sell2
        # n = len(prices)
        # if n == 1: return 0
        # k = 2
        # buy = [float('-inf')] * (n+1) # for convenience
        # sell = [0] * (n+1)
        # for p in prices:
        #     for i in range(1, k+1):
        #         buy[i] = max(buy[i], sell[i-1] - p) # 今天買下去之後剩餘利潤 = 前一天賣完後的利潤扣掉今天的價格
        #         sell[i] = max(sell[i], buy[i] + p) # 今天賣下去之後的利潤 = 今天買下來的剩餘利潤 + 今天的價格
        # return sell[k]
            
        
        # dp_i_1_0, dp_i_1_1 = 0, float('-inf')
        # dp_i_2_0, dp_i_2_1 = 0, float('-inf')
        # for p in prices:
        #     dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + p)
        #     dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - p)
        #     dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + p)
        #     dp_i_1_1 = max(dp_i_1_1, -p)
        # return dp_i_2_0
        
        n = len(prices)
        if n == 1: return 0
        k = 2
        buy = [float('-inf')] * (n+1)
        sell = [0] * (n+1)
        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - p)
                sell[i] = max(sell[i], buy[i] + p)
        return sell[k]