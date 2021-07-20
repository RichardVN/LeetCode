"""
Approach:  DFS traverse and flip
    - Base:  outside bounds or NOT starting color
    - Recursive:  we at start color
        - Flip color
        - Recursive call on neighbors

Similar to number islands.

NOTE: make sure to check start color is not same as newColor

TIME:  O(N)  where N is number pixels
SPACE:  O(N) call stack

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # no rtype. just alter matrix.
        def dfs_fill(image, sr, sc, start_color, newColor):
            # base case. Outside bounds or NOT at start color
            if sr >= len(image) or sr < 0 or sc >= len(image[0]) or sc < 0 or image[sr][sc] != start_color:
                return
            # recursive case At start color. process by flip color, call fill on adjacent
            image[sr][sc] = newColor
            # call in 4 directions
            dfs_fill(image, sr + 1, sc, start_color, newColor)
            dfs_fill(image, sr - 1, sc, start_color, newColor)
            dfs_fill(image, sr, sc + 1, start_color, newColor)
            dfs_fill(image, sr, sc - 1, start_color, newColor)
            return
            
            
        # SHELL
        if not image:
            return None
        R = len(image)
        C = len(image[0])
        # get color of starting point
        start_color = image[sr][sc]
        
        # EDGE case. New color same as old color, check to avoid infinite recursion
        if start_color == newColor:
            return image
        
        # call dfs fill on starting point
        dfs_fill(image, sr, sc, start_color, newColor)
        
        return image