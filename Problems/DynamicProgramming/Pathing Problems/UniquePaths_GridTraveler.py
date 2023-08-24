"""
Time:   O(M X N) possible states
Space:  O(M x N)  memoization
"""
# Recursive  (top-down)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        'how many paths to FINISH from (r,c)'
        def dp(r, c):
            # invalid
            if r < 1 or r > m or c < 1 or c > n:
                return 0
            # base: we are same row or col as finish
            if r == m or c == n:
                return 1
            
            # recursive decions towards base
            # right
            right = dp(r, c + 1)
            # down
            down = dp(r + 1, c)
            return right + down
        return dp(1, 1)
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        'how many paths to end for given grid M X N'
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
    'at memo[r][c] :  How many ways to get to cell (r,c) from START?'
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for _ in range(n)] for _ in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                memo[r][c] = memo[r - 1][c] + memo[r][c - 1]

        # TODO: not that a problem of (m,n) is stored in [m-1][n-1]
        return memo[m-1][n-1]