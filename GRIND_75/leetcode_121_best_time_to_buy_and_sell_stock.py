# Brute Force Solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

# Optimal Solution


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
