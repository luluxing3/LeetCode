class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPrice)
            minPrice = min(prices[i], minPrice)
        return maxProfit
