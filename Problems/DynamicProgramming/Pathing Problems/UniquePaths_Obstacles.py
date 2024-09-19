class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        " given current state r, c .. how many paths to finish?"
        @lru_cache(None)
        def dp(r, c):
            # invalid base
            if r > finishR or c > finishC or obstacleGrid[r][c] == 1:
                return 0
            # smallest valid case
            if r == finishR and c == finishC:
                return 1
            # recursive relation, decisions toward base
            downWays = dp(r + 1, c)
            rightWays = dp(r, c + 1)
            return downWays + rightWays

        finishR = len(obstacleGrid) - 1
        finishC = len(obstacleGrid[0]) - 1
        if obstacleGrid[finishR][finishC] == 1:
            return 0
        return dp(0,0)