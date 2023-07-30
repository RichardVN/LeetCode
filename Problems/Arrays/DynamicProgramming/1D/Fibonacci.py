"""
Key Recursive Relation:  fib(n) = fib(n-1) + fib(n-2)

Time: O(N)  each number up to N is solved once, then cached for later
Space: O(N)  memoization and call stack
"""

# 1a. recursive memoization with dict
class Solution:
    def fib(self, n: int) -> int:
        def dfs(n):
            if n in memo:
                return memo[n]
            if n < 2:
                return n
            # cache answer
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]

        memo = {}
        return dfs(n)
    
# 1b. recursive memoization with array
class Solution:
    def fib(self, n: int) -> int:
        def dfs(n):
            if memo[n]:
                return memo[n]
            # Recursive base cases, these aren't cached in memo
            if n < 2:
                return n
            # cache answer 
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]

        memo = [None for _ in range(n+1)] # n + 1 so we have [0, n] inclusive
        return dfs(n)
        
# 2. Tabulation: bottom - up
class Solution:
    def fib(self, n: int) -> int:
        # edge cases for very small problems
        if n <= 1: return n

        memo = [None for _ in range(n+1)] # n + 1 so we have [0, n] inclusive
        
        # base subproblems
        memo[0] = 0
        memo[1] = 1

        # cache subproblems past base
        for m in range(2, len(memo)):
            memo[m] = memo[m-1] + memo[m-2]
        
        return memo[n]

# 2b. Tabulation with limited variables
class Solution:
    def fib(self, n: int) -> int:
        # edge cases for very small problems
        if n <= 1: return n

        memo = [None for _ in range(n+1)] # n + 1 so we have [0, n] inclusive
        
        # base subproblems
        prev2 = 0
        prev1 = 1

        curr = None
        # cache subproblems past base
        for m in range(2, n+1):
            # solve using previous subproblem answers
            curr = prev2 + prev1
            # update running variables
            prev1, prev2 = curr, prev1
        
        return curr
        