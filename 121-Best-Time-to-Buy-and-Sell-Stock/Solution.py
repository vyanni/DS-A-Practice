class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0

        for num in prices:
            minPrice = min(minPrice, num)
            maxProfit = max(maxProfit, num - minPrice)
        
        return maxProfit