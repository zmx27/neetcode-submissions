class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(prices[sell] - prices[buy], profit)
            else:
                buy = sell # Found cheaper buy price
            sell += 1 # Keep going to see if can sell for lower
        return profit