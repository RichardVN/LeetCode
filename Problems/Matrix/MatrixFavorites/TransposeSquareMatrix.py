"""
Transpose matrix = flip across main diagonal
We can do in place if it is a square matrix
NOTE: the key is to swap matrix[i][j] with matrix[j][i]. 
    The inner for loop must go from i up to N.

Time: O(N) where there are N elements
Space: O(1)
"""

def transpose_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        # TODO: j starts at i, on the diagonal where j == i,   so we don't end up swapping back to original
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    transpose_matrix(m)
    for row in m:
        print(row)