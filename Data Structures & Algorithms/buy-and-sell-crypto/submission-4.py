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

    def maxProfitDP(self, prices: List[int]) -> int:
        # Keep track of lowest price so far, best profit so far
        lowest_price = prices[0]
        best_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - lowest_price
            best_profit = max(profit, best_profit)
            lowest_price = min(lowest_price, prices[i])
        return best_profit
