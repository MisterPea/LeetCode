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

