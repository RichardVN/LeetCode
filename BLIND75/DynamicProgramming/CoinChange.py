# https://leetcode.com/problems/coin-change/
"""
Intuition:  each amount problem can be solved by smaller subproblems
    ex.  change for 10 cents can be 1(nickel) + subproblem: change for 5 cents

Bottom Up:  solve change for amount 0, 1, etc...

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set up dp array for every subproblem (amount to change)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # step thru each subproblem
        for a in range(1, amount + 1):
            for c in coins:
                # if this coin fits into this amount
                if a - c >= 0:
                    # pick lowest change possible
                    dp[a] = min(dp[a], 1+ dp[a-c])

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]