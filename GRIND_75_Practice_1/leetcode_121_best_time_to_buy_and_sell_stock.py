class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = 10**4 + 1
        for price in prices:
            if price < min_price:
                min_price = price
            if (price - min_price) > max_profit:
                max_profit = price - min_price
        return max_profit

# Improved Version
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # can consider the first indexed price as min_price.
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))