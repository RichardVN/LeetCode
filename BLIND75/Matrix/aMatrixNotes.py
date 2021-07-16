""" Initialize matrix. Start with inner array (row) are nested in inside"""
R = 2
C = 3
matrix = [[0 for c in range(C)] for r in range(R)]

""" Get Dimensions """
R = len(matrix)
C = len(matrix[0])


""" If we want to traverse row by row, we have rows on outer loop"""
for r in range(R):
    for c in range(C):
        pass

""" if we want to traverse column by column, we have cols on outer loop """
for c in range(C):
    for r in range(R):
        pass

""" We want to do stuff with a specific column """
# iterate over all row spots in this column
for r in range(R):
    matrix[r][2] = 8

"""
Transpose matrix across diagonal (non Square):
    - Make new C X R matrix of zeroes
    - iterate over m1, assign m2[c][r] = m1[r][c]

Transpose matrix across diagonal (square)
    - If it is square, we can do O(1) space by using swaps ..
        - inner loop j iterates from i to N  (diagonal to end of row)
"""
print(matrix)