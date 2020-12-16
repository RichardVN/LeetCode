"""
Time: O(n)
Space: O(1)
# NOTE: we only need max_profit, NOT days/indices of when to sell, buy
# NOTE: consider the best profit available with each increasing day

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lowest = prices[0]
        max_profit = 0

        # we don't need to modify, or access indices
        for price in prices:
            lowest = min(lowest, price)
            profit = price - lowest
            max_profit = max(profit, max_profit)

        return max_profit
