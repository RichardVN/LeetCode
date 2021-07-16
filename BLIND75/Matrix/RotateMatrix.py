"""
Intuition:
    - notice that the output after rotate, that the rows are now columns
    - we can transpose (but the columns will be out of order)
    --> loop thru each row and reverse so that the columns will be in order

Time: O(N) to transpose, O(N) to reverse
space: O(1) transpose and reverse done via swapping in place
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def reverse(A):
            l = 0
            r = len(A) - 1
            while l < r:
                A[l], A[r] = A[r], A[l]
                # Update ptrs
                l += 1
                r -= 1
            
        # 1. Transpose matrix 
        # NOTE: this is nxn square so we can do in place
        N = len(matrix)

        for r in range(N):
            for c in range(r, N):       # we start at c = r, on the diagonal
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                    
        # 2. Go thru each row and reverse
        R = len(matrix)
        for r in range(R):
            reverse(matrix[r])
        