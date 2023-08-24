"""
Take / Skip :  we can advance to next "state" by inaction ... adjust i but not constraint

Non-For loop:
    - Include Invalid base case (i index)
    - Include recursive call for "skipping" candidate[i]

For Loop:
    - loop from current i to end of candidates
    - No need to include Invalid base case, or Skip recursive call.
"""
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(i, amount):
            # TODO: base: INCLUDES invalid i case
            if i >= len(coins) or amount <0:
                return 0
            # Succeed base case:
            if amount == 0:
                return 1

            # take or not take DECISION
            take = dp(i, amount - coins[i]) # Take w/ repeats:  dfs(same i, changed constraint)
            skip = dp(i+1, amount) # TODO: have to include skip option
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