"""

Decision Tree:
- What to pass down "state" of problem (params?):
    - i  :  index of candidates we have considered
    - bought? :  bool of whether we are in bought state
- what to return up?:
    - maxProfit of smaller subproblems

TIME:  O(2N) ... solve for each index twice (bought / not bought)
SPACE: O(2N)  cache 

"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dfs(i, isBought):
            # check cache
            if (i, isBought) in memo:
                return memo[(i, isBought)]
            # base:
            if i >= len(prices):
                return 0
            # recursive decision tree
            # 1. BOUGHT state: decide to sell or skip day and keep stock
            if isBought:
                memo[(i, isBought)] = max(dfs(i+1, False) + prices[i] , dfs(i+1, True)) 
            # 2. NOT BOUGHT state:  decide to buy, or skip day with no stocks
            else:
                memo[(i, isBought)] = max(dfs(i+1, True) - prices[i] - fee , dfs(i+1, False))

            return memo[(i, isBought)]
        
        memo = {}
        return dfs(0 , False)
    

"""
iterative bottom - up
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dfs(i, isBought):
            # check cache
            if (i, isBought) in memo:
                return memo[(i, isBought)]
            # base:
            if i >= len(prices):
                return 0
            # recursive decision tree
            # 1. BOUGHT state: decide to sell or skip day and keep stock
            if isBought:
                memo[(i, isBought)] = max(dfs(i+1, False) + prices[i] , dfs(i+1, True)) 
            # 2. NOT BOUGHT state:  decide to buy, or skip day with no stocks
            else:
                memo[(i, isBought)] = max(dfs(i+1, True) - prices[i] - fee , dfs(i+1, False))

            return memo[(i, isBought)]

        # initialize memo
        memo = [[0,0] for _ in range(len(prices) + 1)] 

        # iterate from base subproblems
        for i in range(len(prices) - 1, -1, -1):
            memo[i][False] =  max(memo[i+1][True] - prices[i] - fee , memo[i+1][False])
            memo[i][True] = max(memo[i+1][False] + prices[i] , memo[i+1][True])

        return memo[0][False]