class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        
        for sell in prices:
            if sell < minBuy:
                minBuy = sell
            else:
                maxP = max(maxP, sell - minBuy)
        return maxP