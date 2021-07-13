class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 1 or k == 0 or not prices: return 0
#         if k >= n/2:
#             # 如果 k 大於 n/2，代表可以做無限次交易（因為做一次交易需要兩天）
#             profit = 0
#             for i in range(1, len(prices)):
#                 if prices[i] > prices[i-1]: profit += prices[i] - prices[i - 1]
#             return profit

#         buy = [float('-inf')] * (n+1) # for convenience
#         sell = [0] * (n+1)
#         for p in prices:
#             for i in range(1, k+1):
#                 buy[i] = max(buy[i], sell[i-1] - p) # 今天買下去之後剩餘利潤 = 前一天賣完後的利潤扣掉今天的價格
#                 sell[i] = max(sell[i], buy[i] + p) # 今天賣下去之後的利潤 = 今天買下來的剩餘利潤 + 今天的價格
#         return sell[k]

        n = len(prices)
        if n == 1 or k == 0 or not prices: return 0
        if k >= n/2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        buy = [float('-inf')] * n
        sell = [0] * n
        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - p)
                sell[i] = max(sell[i], buy[i] + p)
        return sell[k]