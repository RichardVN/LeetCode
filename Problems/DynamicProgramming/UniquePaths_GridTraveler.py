"""
Time:   O()
Space:  O(M x N)  memoization
"""
# Recursive  (top-down)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(m,n):
            if (m,n) in memo:
                return memo[(m,n)]
            if m == 0 or n == 0:
                return 0
            if m == 1 or n == 1:
                return 1
            # go right or down
            memo[(m,n)] = dfs(m-1,n) + dfs(m, n-1)
            return memo[(m,n)]
        
        memo = {}

        return dfs(m,n)
    

"""
Tabulation Solution
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for _ in range(n)] for _ in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                memo[r][c] = memo[r - 1][c] + memo[r][c - 1]

        # TODO: not that a problem of (m,n) is stored in [m-1][n-1]
        return memo[m-1][n-1]