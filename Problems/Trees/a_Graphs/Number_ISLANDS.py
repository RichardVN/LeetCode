"""
DFS approach: Iterate thru matrix. DFS tranverse convert 1->0 upon hitting a 1
    - Call a flood fill transform land to water upon hitting land. Keep count

Time: O(M x N)
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
        # expands and touches every element in matrix
        # helper recursive. Traverse "island" convert to 0. No return type just DO
        def dfs_traverse(grid,r,c):
            # base case: outside bounds of grid, or we or on water. Access indices AFTER
            if r >= R or r < 0 or c >= C or c < 0 or grid[r][c] == "0" :
                return
            # recursive case. Call traverse on "children" / neighbors. Process Current
            # 1. Process. convert to 0
            grid[r][c] = "0"
            # 2. Recursively call on neighbor in all directions
            dfs_traverse(grid, r-1, c)
            dfs_traverse(grid, r+1, c)
            dfs_traverse(grid, r, c-1)
            dfs_traverse(grid, r, c+1)
            
            # 3. nothing to return, changed grid 
            
        # Main function shell
        # empty edge case:
        if not grid:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        
        num_islands = 0
        
        for r in range(R):
            for c in range(C):
                # check if land
                if grid[r][c] == "1":
                    # traverse starting with r,c as root. Set land to 0
                    dfs_traverse(grid, r, c)
                    # increment found island
                    num_islands += 1
        
        return num_islands
        