"""

Time: O(N)  each number up to N is solved once, then cached for later
Space: O(N)  memoization and call stack
"""

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
        