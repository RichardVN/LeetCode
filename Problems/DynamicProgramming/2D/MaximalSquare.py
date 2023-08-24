"""
'What is maximalSquare SIDE with (r,c) as top-left corner?'

A 3x3 maximal square can only be formed if 2x2 squares can be formed in Right, Diag, and Down

Helper function to solve for MaximalSquare SIDE LENGTH

Time: O(M * N)
Space: O(M * N)
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def dp(r,c):
            if (r,c) in memo:
                return memo[(r, c)]

            if (
                r < 0 or 
                c < 0 or
                r >= len(matrix) or
                c >= len(matrix[0]) 
            ):
                return 0
            
            # we still want to calculate for other squares, even if not at '1'
            rightMaxLen = dp(r, c+1)
            diagMaxLen = dp(r+1, c+1)
            downMaxLen = dp(r+1, c)

            if matrix[r][c] == '1':
                memo[(r,c)] = 1 + min(rightMaxLen, diagMaxLen, downMaxLen)
                return memo[(r,c)]
            else:
                memo[(r,c)] = 0
                return memo[(r,c)]
        
        memo = {}
        dp(0,0)
        return max(memo.values())**2