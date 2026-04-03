class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r  = 0, 1
        result = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                currentPrices = prices[r] - prices[l]
                result = max(result, currentPrices )
            else:
                l = r
            r += 1
        return result


        