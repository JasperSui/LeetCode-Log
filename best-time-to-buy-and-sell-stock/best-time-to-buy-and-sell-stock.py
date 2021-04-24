class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])
        return dp_i_0
        
        # if not prices: return 0
        # min_price, max_profit = prices[0], 0
        # for i in range(1, len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        # return max_profit
        
        # Suck idea
        # min_price, min_index = float('inf'), None
        # max_price, max_index = float('-inf'), None
        # max_profit = 0
        # if not prices: return 0
        # for i, p in enumerate(prices):
        #     if p <= min_price:
        #         min_price = p
        #         min_index = i
        #     elif p >= max_price or p >= min_price:
        #         max_price = p
        #         max_index = i
        #     if min_index is not None and max_index is not None and min_index < max_index:
        #         print(min_index, max_index)
        #         max_profit = max(max_profit, max_price-min_price)
        # return max_profit
        
        # if not prices:
        #     return 0
        # min_price, max_profit = prices[0], 0
        # for i in range(1, len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        # return max_profit