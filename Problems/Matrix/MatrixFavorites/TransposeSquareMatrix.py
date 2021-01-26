def transpose_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        # TODO: start at column i, or else we just end up with original array
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