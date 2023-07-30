"""
- Similar to num Islands, call dfsFlood() when encounter a '1'
    - * we could just add (r,c) to set, if dont want to modify original grid
- NOTE: make sure to calculate the local area of single island, not total area of all islands 
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # flood and count squares flooded for THIS island
        def dfs(r,c):
            if (
                r < 0 or
                r >= numRows or
                c < 0 or 
                c >= numCols
                or grid[r][c] != 1
            ): return 

            nonlocal islandArea
            nonlocal maxArea

            islandArea += 1
            maxArea = max(maxArea, islandArea)

            grid[r][c] = 0 #NOTE: alternatively, add (r, c) to "seen" set
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        maxArea = 0

        numRows = len(grid)
        numCols = len(grid[0])

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    islandArea = 0
                    dfs(r,c)

        return maxArea