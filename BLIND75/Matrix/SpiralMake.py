"""
NOTE: There is no break boundary check after Right:
        - we are N x N matrix, if boundaries are invalid then 
            for(right,left,-1) will be invalid and not execute
        - if top and bottom invalid, then so will left and right because same dimension
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # instantiate matrix
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        # instantiate boundaries
        left = top = 0
        right = bottom = n - 1
        
        next_num = 1
        
        while left <= right and top <= bottom:
            # top layer:  left to right
            for c in range(left, right + 1):
                matrix[top][c] = next_num
                next_num += 1
            top += 1
            
            # right layer: top to bottom
            for r in range(top, bottom + 1):
                matrix[r][right] = next_num
                next_num += 1
            right -= 1
            
            # bottom layer:  right to left
            for c in range(right , left -1, -1):
                matrix[bottom][c] = next_num
                next_num += 1
            bottom -= 1
            
            # left layer:  bottom to top
            for r in range(bottom, top-1 , -1):
                matrix[r][left] = next_num
                next_num += 1
            left += 1
            
        return matrix
        