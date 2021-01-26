def transpose_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        # TODO: start at column i, or else we just end up with original array
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
