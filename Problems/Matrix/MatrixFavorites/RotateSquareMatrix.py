# https://leetcode.com/problems/rotate-image/
"""
What does 'rotate' mean?
- note that rows are now columns => Think TRANSPOSE
- but we have to reverse the order of column elements

Pseudo:
    1. transpose square matrix over main diagonal
    2. for each row in matrix, reverse elements in row
        * create a helper function that reverses a 1D array row, or use .reverse()

Time: O(N) to transpose, O(N) to reverse
Space: O(1), in-place transpose and reversals
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def reverse_row(row, l, r):
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
        
        # SQUARE matrix, we can transpose in place
        N = len(matrix)
        for r in range(N):
            # from diagonal to end of row
            for c in range(r, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # have to reverse each row (list)
        for r in range(N):
            reverse_row(matrix[r], 0, N-1)  #NOTE: use .reverse() if allowed

        return matrix