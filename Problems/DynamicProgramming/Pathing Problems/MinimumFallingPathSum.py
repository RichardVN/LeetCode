"""
'what is minFallingPathSum  from  r,c'

State:
- r , c

Recursive Relation:
- dp(r,c) = MIN (left, right , down)  +  grid[r][c]

"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(r, c):
            # base invalid
            if r < 0 or c < 0 or r >= rowLen or c >= colLen:
                return float('inf')
            if r == rowLen - 1:
                return matrix[r][c]
            # recursive decisions based off traversal
            return matrix[r][c] + min(dp(r+1, c), dp(r+1, c+1) , dp(r+1, c-1))
        
        rowLen = len(matrix)
        colLen = len(matrix[0])
        
        # iterate thru first row
        minPathSum = float("inf")
        for c in range(colLen):
            minPathSum = min( minPathSum, dp(0, c))
        return minPathSum
            
        