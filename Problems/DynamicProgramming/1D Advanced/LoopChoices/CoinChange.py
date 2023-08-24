from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # subproblem ... For given amt, what is MIN number of coins?
        # inf of each coin, therefore each subproblem: look at all coins
            # therefore we dont need to pass in i index.
        @lru_cache(None)
        def dfs(amount):
            # base
            if amount == 0 : return 0
            # base invalid
            if amount < 0: return float("inf")
            # recursive relation
            minCoins = float("inf")
            # check all coin options
            for coin in coins:
                minCoins = min(minCoins, dfs(amount - coin) + 1)

            return minCoins

        res = dfs(amount)
        return res if res != float("inf") else -1

        """ NOTE: We can be more selective with For loop to only include UNIQUE combinations"""
        @lru_cache(maxsize=amount*len(coins))
        def dfs1(i, amount):
            # base
            if amount == 0 : return 0
            # base invalid
            if amount < 0: return float("inf")
            # recursive relation
            minCoins = float("inf")
            # check all coin options
            for j in range(i, len(coins)):
                # take. Repeats allowed -> (same i, changed constraint)
                minCoins = min(minCoins, dfs(j, amount - coins[j]) + 1)
            return minCoins

        res = dfs(0,amount)
        return res if res != float("inf") else -1