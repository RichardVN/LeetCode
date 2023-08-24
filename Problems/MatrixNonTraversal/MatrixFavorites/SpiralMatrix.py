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
        # result
        res = []
        
        # boundaries are inclusive
        top = 0
        left = 0 
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        
        while bottom >= top and right >= left:
            # top layer: at top, move left to right, increment top
            for column in range(left, right+1):
                res.append(matrix[top][column])
            top += 1
    
            # right layer: at right, move top to bottom, decrement right
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # TODO: We are about to repeat horizontal and vertical movement, check boundaries again
            if not (bottom >= top and right >= left):
                break
            
            # bottom layer: at bottom, move right to left, decrement bottom
            for column in range(right, left -1 , -1):
                res.append(matrix[bottom][column])
            bottom -= 1
            
            # left layer: at left, move bottom to top, increment left
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1
                
        return res