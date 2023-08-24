"""
"how Many ways?" ->  a COMBINATIONS question:
- Combination matters, so we cannot just loop through all coins cuz we will get repeats
- start with backtrack template -> DP

Time: O(N * Amount)   ... number of states in parameters
Space: O(N * Amount)
"""
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(i, amount):
            # base success
            if amount == 0:
                return 1
            # Base invalid
            if amount < 0 or i == len(coins):
                return 0
            
            # TAKE ... repeats allowed
            take = dp( i , amount - coins[i])
            # SKIP this choice
            skip = dp( i+1 , amount)
            return take + skip

        return dp(0, amount)

    
    """ version with for loop """
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(i, amount):
            # TODO: base: no need for invalid i case
            if amount < 0:
                return 0
            # Succeed base case:
            if amount == 0:
                return 1

            # loop version from current i to end of candidates
            numWays = 0
            for j in range(i, len(coins)):
                numWays += dp(j, amount - coins[j]) # pass in same i because repeats are allowed
            # TODO: loop inherently does the SKIP option  dp(i+1, amount)
            return numWays

        return dp(0, amount)