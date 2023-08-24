"""
- Invalid state if dupe in same row, same col, or same "box"
NOTE:  when checking dupes -> Think HASH SET
    - create hash set for each row and col, and the 9 blocks
- For any R,C cell .. how do we know if we're in a particular box?
    - Think of the boxes as a 3x3 grid
    - Each box is uniquely identified by (box_row, box_col),  which is row//3, col//3

seenInRow: {
   row -> { set of numbers in row }
}
seenInBox {
    (box_r, box_c)  ->  {set of numbers in box }
}

Time:  O(R X C)
Space: O(R X C) for full board

"""

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenInRow = defaultdict(set)
        seenInCol = defaultdict(set)
        seenInBox = defaultdict(set)    # the Key will be (box_row, box_col)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                # first check if this is "empty space"
                if num == ".":
                    continue

                box_r = r // 3
                box_c = c // 3
                num = board[r][c]

                if num in seenInRow[r] or num in seenInCol[c] or num in seenInBox[(box_r, box_c)]:
                    return False
                else:
                    seenInRow[r].add(num)
                    seenInCol[c].add(num)
                    seenInBox[(box_r, box_c)].add(num)
        return True
