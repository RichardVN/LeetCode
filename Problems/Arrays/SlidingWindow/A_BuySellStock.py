"""
# NOTE: we only need max_profit. We don't need the day/indices of when to buy or sell
# NOTE: This is "Dynamic Programming". The solution to the Whole problem, can be deduced from solution of smaller subproblems.

NOTE: we can only sell AFTER we buy
            => We keep track of smallest seen so far to the LEFT

Intuition:
    1. Variables to track "lowest seen so far" and "biggest profit so far"
    2. Iterate through nums
        - If num is a new low, update lowest. We Do not buy on a minimum
        - Num is NOT a new low, we check if we can make a bigger profit
    3. Return the max profit after going through all nums

Time: O(n)
Space: O(1)

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lowest_seen = prices[0]
        max_profit = 0

        # we don't need to modify, or access indices
        for price in prices:
            lowest_seen = min(lowest_seen, price)
            profit = price - lowest_seen
            max_profit = max(profit, max_profit)

        return max_profit


"""
Sliding Window approach
NOTE: once we encounter a new minimum, that is optimal day to buy from then on, adjust left pointer

Intuition:
    - Iterate through array with R (sell)
    - If we see a new minimum, set L (buy) to current
    - If not minimum, try to sell and see if it's a higher profit
"""
class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        l = 0
        r = 0

        max_profit = 0
        lowest_seen = float(inf)

        while r < len(prices):
            if prices[r] < lowest_seen:
                lowest_seen = prices[r]
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            r += 1
        
        return max_profit
            
