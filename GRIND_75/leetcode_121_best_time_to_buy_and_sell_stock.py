class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if (price - min_price) > max_profit:
                max_profit = price - min_price
        return max_profit


# s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))

# s = Solution()
# print(s.maxProfit([7, 6, 4, 3, 1]))
