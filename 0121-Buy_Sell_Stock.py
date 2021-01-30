# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        pointer_a = 0
        max_profit = 0
        for pointer_b in range(1, len(prices)):
            current_profit = prices[pointer_b] - prices[pointer_a]
            max_profit = max(current_profit, max_profit)
            if prices[pointer_a] >= prices[pointer_b]:
                pointer_a = pointer_b
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
s = Solution().maxProfit(prices)

