"""
Recursive Top-Down Memoization
"""

class Solution:
    def fib(self, n: int) -> int:
        # helper dfs function.  NOTE: parameters contain the "state" of the subproblem. E.g. item index, bought/not bought
        def dfs(n):
            # 1. Check if our subproblem is cached
            if memo[n]:
                return memo[n]
            # 2a. base cases that don't need to be cached. What to return if out-of-bounds i
            if n < 2:
                return n
            # 2b. Solve non-base subproblems, and cache in memo. #TODO: recursive relation here
            memo[n] = dfs(n-1) + dfs(n-2)   # Commonly: Summation ways from subproblems, min/max optimize from subproblem choices
            return memo[n]
        # initialize a shared memo cache outside of dfs helper
        memo = [None for _ in range(n+1)] # n + 1 so we have [0, n] inclusive
        return dfs(n)   # NOTE: return answer to subproblem

"""
Iterative Bottom-Up Tabulation
"""

class Solution:
    def fib(self, n: int) -> int:
        # 1. edge cases for very small problems
        if n <= 1: return n

        # 2. Initialize memo cache for subproblems
        memo = [None for _ in range(n+1)] # n + 1 so we have [0, n] inclusive
        
        # 3a. base subproblems
        memo[0] = 0
        memo[1] = 1

        # 3b. cache subproblems past base indices to length of memo. #TODO: recursive relation here
        for m in range(2, len(memo)):
            memo[m] = memo[m-1] + memo[m-2]
        
        # return the last value in the memo
        return memo[-1]

"""
Iterative Bottom-Up  with Limited Variables
"""
class Solution:
    def fib(self, n: int) -> int:
        # 1. edge cases for very small problems
        if n <= 1: return n

        memo = [None for _ in range(n+1)] # n + 1 so we have [0, n] inclusive
        
        # 2. Initialize variables to hold previous subproblem answers. Initally has BASE answers
        prev2 = 0
        prev1 = 1

        curr = None
        # 3b. Solve for subproblems past base
        for m in range(2, n+1):
            # solve curr problem using previous subproblem answers
            curr = prev2 + prev1        #TODO: recursive relation here
            # update running variables
            prev1, prev2 = curr, prev1
        
        return curr