"""
General DP template

1. Identify as a DP problem
    - Problem Type: optimization? How many ways? Is Possible?
    - Problem can be solved with overlapping subproblems. Repeated work!

2. Identify the "state" and return Answer of each subproblem
    - State/Constraint Variables -> function Parameters:
        - e.g. index i of candidate, isBought state
    - Return Type:  max/min (int),  isPossible?(Bool)
    TODO: Rephrase problem In English:  'What is the maxScore possible for given state'?

3. Create Base Cases
    - Invalid Base cases using CONSTRAINT of state variables
        - (for min/max INVALID... use float("inf"))
    - SMALLEST valid Base Case which represents the smallest valid answer

4. Recursive Relation:  make decisions and recursively call towards smaller basecase
    - For each valid choice:  make a recursive dp call and pass in New State
    - Think about how smaller subproblem solves THIS problem
    TODO: Rephrase Recursive relation in English
"""



"""
Recursive Top-Down Memoization
"""
from functools import lru_cache
class Solution:

    def fib(self, n: int) -> int:
        # helper dfs function.  
        @lru_cache(None)
        def dfs(n): # TODO: pass down STATE variables (E.g. item index, currSum)
            # Base Case: that don't need to be cached. What to return if out-of-bounds i
            if n < 2:
                return n
            # Recursive: Solve THIS subproblem by recursing into SMALLER subproblem. Cached in memo. 
            return dfs(n-1) + dfs(n-2)   # #TODO: recursive relation here (Summation ways from subproblems, min/max optimize from subproblem choices)
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

        # 3b. cache subproblems past base indices to length of memo. #TODO: recursive relation here ... same as recursive
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