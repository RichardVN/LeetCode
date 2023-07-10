"""

1 - Binary search to narrow down the targetRow
2 - Binary search within targetRow to find target
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        # Binary search to find the targetRow that should contain target
        rtop = 0
        rbot = R - 1

        targetRow = None
        while rtop <= rbot:
            rmid = rtop + (rbot - rtop) // 2
            midRow = matrix[rmid]
            # target in row below
            if target > midRow[-1]:
                rtop = rmid + 1
            elif target < midRow[0]:
                rbot = rmid - 1
            # target is between midRow[0] and midRow[-1]
            else:
                targetRow = midRow
                break

        # TODO: case where targetRow never got set b/c never hit else cause
        if not targetRow:
            print("not target row")
            return False
        
        # Binary search to find target within targetRow
        l = 0
        r = len(targetRow) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if target == targetRow[mid]:
                return True
            elif targetRow[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False