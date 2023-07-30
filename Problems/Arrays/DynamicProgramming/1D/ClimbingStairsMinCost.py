"""
Top-Down Recursion with Memoization: 

Time: O(N) Each subproblem from 0 to N is solved only once
Space:  O(N)  for cache and call stack

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            # is our subproblem cached? Cached answer is guaranteed to be optimal
            if i in memo:
                return memo[i]
            # base subproblem... 1st 2 steps
            if i <= 1:
                return 0
            # recursive case Subproblem: cost to get to ith step
            bestCost = min( dfs(i-2) + cost[i-2] , dfs(i-1) + cost[i-1] )
            memo[i] = bestCost
            return memo[i]
            

        memo = {}
        # dfs for one index past COST[] ... aka "Top"
        return dfs(len(cost))



"""
Bottom-Up Tabulation
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # trivial base
        if len(cost) <= 1:
            return 0
        # initialize memo with trivial base cases
        memo = [0 for i in range(len(cost) + 1)]
        memo[0] = memo[1] = 0

        # solve subproblem above base, thru length memo
        for i in range(2, len(memo)):
            memo[i] = min ( memo[i-2] + cost[i-2], memo[i-1] + cost[i-1] )
        return memo[-1]
