"""
Work Backwards:  start dfsTraversal from each cell that is adjacent to the "oceans"

# function signature
# NOTE: visited is a set() of (r,c) tuples ... pass in either pac / atl
# NOTE: we flow "up" ... heights[r][c] is LESS than prevHeight, then invalid
dfs(r, c, visited, prevHeight)

TIME: O(4 * M x N)
Space: O(M x N) for sets
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # visited is a set() .. either atl or pac
        def dfs(r,c, visited, prevHeight):
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                heights[r][c] < prevHeight or
                (r,c) in visited
            ): return
            # valid flow up
            visited.add((r,c))
            dfs(r+1, c , visited, heights[r][c])
            dfs(r-1, c , visited, heights[r][c])
            dfs(r, c+1 , visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            return 

        # set: (r,c)
        pac, atl = set(), set()

        # list of lists
        res = []

        rows = len(heights)
        cols = len(heights[0])

        # flow from top and bottom row ... spread and mark valid cells.
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # pacific top row
            dfs(rows - 1 , c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        # find overlap in sets
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res