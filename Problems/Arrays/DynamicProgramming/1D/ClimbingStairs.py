"""
Key Recursive Relation:  stairs(n) = stairs(n-1) + stairs(n-2)
" Distinct ways climb n steps == distinct ways climb n - 1 steps + distinct ways climb n - 2 steps "

"""
# recursive with dict memo
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n):
            # check if in cache
            if n in memo:
                return memo[n]
            # base cases / subproblems
            if n == 1 :
                return 1
            if n == 2:
                return 2
            memo[n] = dfs(n-1) + dfs(n-2) # TODO: recursive relation
            return memo[n]
        
        memo = {}
        return dfs(n)

# iterative:  bottom-up tabulation 
class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 1: return 1
        if n == 2: return 2

        # tabulation with base subproblems
        memo = [0 for _ in range(n+1)]
        memo[1] = 1
        memo[2] = 2

        # cache subproblems past base
        for i in range(3, len(memo)):
            memo[i] = memo[i-1] + memo[i-2]  # TODO: recursive relation
        return memo[n]

# iterative with few variables
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev_1 = 2
        prev_2 = 1

        curr = None

        # solve subproblems unti N
        for N in range(3, n+1):
            curr = prev_1 + prev_2
            prev_1 , prev_2 = curr, prev_1
        
        return curr