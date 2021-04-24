class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, n = 0, len(prices) - 1 
        buy, sell, profit = 0, 0, 0
        while i < n:
            while i < n and prices[i+1] <= prices[i]: i += 1
            buy = prices[i]
            while i < n and prices[i+1] >= prices[i]: i += 1
            sell = prices[i]
            
            profit += sell - buy
        return profit