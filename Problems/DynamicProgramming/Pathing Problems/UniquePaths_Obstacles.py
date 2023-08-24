class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        " given current state r, c .. how many paths to finish?"
        @lru_cache(None)
        def dp(r, c):
            # succeed base
            if r == finishRow and c == finishCol:
                return 1
            # invalid
            if r > finishRow or r < 0 or c > finishCol or c < 0 or obstacleGrid[r][c] == 1:
                return 0
            
            # traversal options
            # move right
            uniquePathsRight = dp(r, c + 1)
            # move down
            uniquePathsDown = dp(r+1, c)
            return uniquePathsRight + uniquePathsDown
        
        # TODO: edge case. finish IS obstacle
        if obstacleGrid[-1][-1] == 1:
            return 0
        
        numRows = len(obstacleGrid)
        numCols = len(obstacleGrid[0])
        
        finishRow = numRows - 1
        finishCol = numCols - 1
        return dp(0, 0)
        