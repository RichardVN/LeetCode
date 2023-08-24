"""
Transpose Matrix  => Have to swap i, j
NOTE: If square, we can flip in-place over main diagonal

Pseudo:
- initialize new matrix, swapping num_rows with num_cols
- traverse over original matrix, and assign value to res matrix (swap r, c)

Time: O(R*C)  elements
Space:  O(R*C) .. O(1) if square matrix
"""

def transpose_square_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        # TODO: j starts at i, on the diagonal where j == i,   so we don't end up swapping back to original
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


"""
Transposing generic matrix into new matrix
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # new matrix has num_col, num_row switched
        m = [[0 for c in range(num_rows)] for r in range(num_cols)]

        # traverse over original matrix
        for r in range(num_rows):
            for c in range(num_cols):
                m[c][r] = matrix[r][c]
        return m