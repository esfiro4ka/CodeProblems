class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = prices[0]
        solding_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                solding_price = prices[i]
            else:
                max_profit += solding_price - buying_price
                buying_price = solding_price = prices[i]
        max_profit += solding_price - buying_price
        return max_profit
        