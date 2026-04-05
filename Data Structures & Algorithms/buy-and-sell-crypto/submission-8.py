class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currentPrice = prices[r] - prices[l]
                result = max(result, currentPrice)
            else:
                l = r
            r += 1
        return result