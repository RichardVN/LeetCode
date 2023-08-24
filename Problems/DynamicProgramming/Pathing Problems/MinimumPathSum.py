"""
Optimize.. MIN path sum

Can only move Down and Right... no backtracking or repeating cells

STATE of problem:
- r, c, currPathSum

Recursive Relation?:
 - dp(r, c) = grid[r][c] + MIN (rightChoice, leftChoice)


"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(r, c):
            # Base smallest
            if r == finishRow and c == finishCol:
                return grid[r][c]
            # base invalid
            if r < 0 or c < 0 or r > finishRow or c > finishCol:
                return float('inf')
            
            # Recursive decisions / relations
            right = dp(r, c+1)
            down = dp(r+1, c)
            return grid[r][c] + min(right, down)
        
        rowLen, colLen = len(grid), len(grid[0])
        finishRow, finishCol = rowLen - 1, colLen -1
        
        # path stum from start 0, 0
        return dp(0, 0)
        