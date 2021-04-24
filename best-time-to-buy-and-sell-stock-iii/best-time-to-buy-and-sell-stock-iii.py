class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one_buy, two_buy = float('inf'), float('inf')
        # one_buy_one_sale, two_buy_two_sale = 0, 0
        # for p in prices:
        #     one_buy = min(one_buy, p)
        #     one_buy_one_sale = max(one_buy_one_sale, p - one_buy)
        #     two_buy = min(two_buy, p - one_buy_one_sale)
        #     two_buy_two_sale = max(two_buy_two_sale, p - two_buy)
        # return two_buy_two_sale
        
        dp_i_1_0, dp_i_1_1 = 0, float('-inf')
        dp_i_2_0, dp_i_2_1 = 0, float('-inf')
        for p in prices:
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + p)
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - p)
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + p)
            dp_i_1_1 = max(dp_i_1_1, -p)
        return dp_i_2_0