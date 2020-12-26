"""
Imagine a Frame
            --- row_begin ---
            |               |
Col Begin   |               | Col_end
            |               |
            --- row_end -----

When we traverse in a "spiral" we 
    1. add elements along ONE SIDE of the frame, 
    2. adjust that side of the frame (decrement by one), so we exclude the values we just read
    NOTE: We need additional IF checks for bottom_row and left_col to ensure that we are still within valid bounds

Time: O(N), where N is all of matrix elements
Space: O(N) including the returned list, O(1) if not including list
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res

        # set frame indices
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1
        col_end = len(matrix[0])-1

        # while the fram top-bottom AND frame left-right are at least equal to same row
        while (row_begin <= row_end and col_begin <= col_end):
            # loop through top row, INCLUSIVE of all columns "+1"
            for i in range(col_begin, col_end+1):
                res.append(matrix[row_begin][i])
            # shift frame-top down
            row_begin += 1

            # loop through right column, INCLUSIVE of all rows
            for i in range(row_begin, row_end+1):
                res.append(matrix[i][col_end])
            # shift frame-right left
            col_end -= 1

            """  
            NOTE: We need "if" statements because we changed row_begin and col_end
                    This might make the next entries invalid before we can make it to the next while loop check """

            # is this bottom row valid
            if (row_begin <= row_end):
                # loop through bottom row, across all columns
                for i in range(col_end, col_begin-1, -1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            # is this column valid
            if (col_begin <= col_end):
                # loop through left column, across all rows
                for i in range(row_end, row_begin-1, -1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res
