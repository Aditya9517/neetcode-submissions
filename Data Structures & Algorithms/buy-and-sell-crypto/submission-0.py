class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = -1

        for price in prices:
            if price < buy:
                buy = price
            maxProfit = max(maxProfit, price-buy)
        return maxProfit
        