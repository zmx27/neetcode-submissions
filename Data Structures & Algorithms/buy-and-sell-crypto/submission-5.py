class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of lowest price so far, best profit so far
        lowest_price = prices[0]
        best_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - lowest_price
            best_profit = max(profit, best_profit)
            lowest_price = min(lowest_price, prices[i])
        return best_profit