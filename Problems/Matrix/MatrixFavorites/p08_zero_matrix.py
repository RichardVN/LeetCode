"""
Pseudo:
    - initialize sets to keep track which c contains a zero, which r contains a zero
    - traverse over matrix... if r or c is in the "zero sets" , set element to 0

Time: O(R*C) to traverse over matrix
Space: O(R + C)  to create hash sets
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsWithZero = set()   # Space: max R rows
        colsWithZero = set()   # Space: max C cols

        numRows = len(matrix)
        numCols = len(matrix[0])

        # determine which row/col contains zero
        for r in range(numRows):
            for c in range(numCols):
                if matrix[r][c] == 0:
                    rowsWithZero.add(r)
                    colsWithZero.add(c)
        # traverse and set zeroes
        for r in range(numRows):
            for c in range(numCols):
                if r in rowsWithZero or c in colsWithZero:
                    matrix[r][c] = 0
        return matrix