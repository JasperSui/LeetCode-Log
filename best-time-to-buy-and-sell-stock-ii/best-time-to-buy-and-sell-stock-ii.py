class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         i, n = 0, len(prices) - 1 
#         buy, sell, profit = 0, 0, 0
#         while i < n:
#             while i < n and prices[i+1] <= prices[i]: i += 1
#             buy = prices[i]
#             while i < n and prices[i+1] >= prices[i]: i += 1
#             sell = prices[i]
            
#             profit += sell - buy
#         return profit

        # dp_i_0, dp_i_1 = 0, float('-inf')
        # for i in range(len(prices)):
        #     temp = dp_i_0
        #     dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        #     dp_i_1 = max(dp_i_1, temp - prices[i])
        # return dp_i_0
        
        i, n = 0, len(prices) - 1
        buy, sell, profit = 0, 0, 0
        while i < n:
            while i < n and prices[i+1] <= prices[i]: i += 1
            buy = prices[i]
            while i < n and prices[i+1] >= prices[i]: i += 1
            sell = prices[i]
            
            profit += sell - buy
        return profit