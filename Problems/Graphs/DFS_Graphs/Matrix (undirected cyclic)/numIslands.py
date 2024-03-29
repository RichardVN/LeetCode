"""
- Traverse through cells of matrix normally
    - IF the cell is '1':
        - Increment island count
        - dfs flood the island
- dfs_flood helper:
    - BASE:  outside of matrix or is not a '1' -> return 
    - Recursive: Flip the cell to 0, call dfs on neighbors

Time: O(M x N)
Space: O(M X N) if dfs stack
Space: O( min(m,n) )  .... each diagonal is level queue in worst case BFS. 
        https://imgur.com/gallery/M58OKvB
    
    RTYPE: no return type, just mutate matrix
    - dfs_traverse(grid, r, c) recursion:
        - Base case: if r,c outside bounds or hit water, just return
        - Recursive Case:
            - Set grid[r][c] to 0
            - Call dfs_traverse in the 4 adjacent grid spots
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # helper recursive. Traverse "island" convert to 0. No return type just DO
        # NOTE: we have access to context of outer function, ex. grid, R, C
        def dfs_traverse(r,c):
            # base case: outside bounds of grid, or we or on water. Access indices AFTER
            if r >= R or r < 0 or c >= C or c < 0 or grid[r][c] == "0" :
                return
            # recursive case. Flip current cell, recursively attempt traverse to neighbors
            # 1. Process. convert to 0
            grid[r][c] = "0"
            # 2. Recursively call on neighbor in all directions
            for x, y in directions:
                dfs_traverse(r+y, c+x)
            # dfs_traverse(r-1, c)
            # dfs_traverse(r+1, c)
            # dfs_traverse(r, c-1)
            # dfs_traverse(r, c+1)
            
            # 3. nothing to return, changed grid 
            
        # Main function shell
        # empty edge case:
        if not grid:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        directions = [(1,0),(-1,0), (0,1), (0, -1)]

        
        num_islands = 0
        
        for r in range(R):
            for c in range(C):
                # check if land
                if grid[r][c] == "1":
                    # traverse starting with r,c as root. Set land to 0
                    dfs_traverse(r, c)
                    # increment found island
                    num_islands += 1
        
        return num_islands

"""
Iterative solution
"""
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsFlood(r,c):
            q = deque([(r,c)])  # TODO: This structure represents the "call stack"

            while q:
                # go to next function call
                r,c = q.popleft()

                # TODO: equivalent to Base case of "function"
                if (
                    r < 0 or
                    r >= rows or
                    c < 0 or
                    c >= cols or
                    grid[r][c] != '1'
                ):
                    continue
                grid[r][c] = '0'

                # TODO: recursively make "function call", by adding new state to stack / queue
                for x,y in directions:
                    newR = r+y
                    newC = c+x
                    q.append((newR, newC))


        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0),(-1,0), (0,1), (0, -1)]

        numIslands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    numIslands += 1
                    dfsFlood(r,c)
        
        return numIslands