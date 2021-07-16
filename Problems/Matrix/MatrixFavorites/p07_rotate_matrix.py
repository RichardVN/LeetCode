# O(NxN)
import unittest
from copy import deepcopy


"""
Intuition:
    - notice that the output after rotate, that the rows are now columns
    - we can transpose (but the columns will be out of order)
    --> loop thru each row and reverse so that the columns will be in order

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
        


def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # empty list of 0s
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [rotate_matrix_pythonic, rotate_matrix]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
