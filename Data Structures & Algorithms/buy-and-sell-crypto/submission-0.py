class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < low:
                low = prices[i]
            if prices[i] > low:
                profit = max(profit,prices[i] - low)
        return profit
        