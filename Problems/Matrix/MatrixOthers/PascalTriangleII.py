"""
NOTE: kth row has around k elements

Intuition:
    - We know that we can calculate the current row with just the previous row
    - We have a base row of [1]
Approach
    1. At all points we keep track of current row and previous row
    2. We initialize the first row as current row
    3. For loop up to and INCLUDING kth row
        a. previous_row is assigned current_row
        b. current_row is assigned to a list of [1] * i number elements
        c. populate current_row using previous_row
    4. return current row (this is k, because we used range(k+1))

Time: It takes constant time to calculate an element from previous row
        Outer loop: k times
        Inner loop: from 1 to k
        Total O(k^2)
Space:
    Two rows O(k) + O(k)  = O(k)
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_prev = []
        row_curr = [1]
        for i in range(rowIndex + 1):
            row_prev[:] = row_curr
            # initialize values to 1 so we dont have to change first and last values
            row_curr[:] = [1] * (i+1)

            # populate middle elements
            for j in range(1, len(row_curr)-1):
                row_curr[j] = row_prev[j] + row_prev[j-1]
        return row_curr
