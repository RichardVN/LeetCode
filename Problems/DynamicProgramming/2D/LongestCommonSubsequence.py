"""
Optimize: longest

' For problem at this STATE: what is LCS'
STATE / parameters:
    i : position in text1
    j : position in text2

return:  (int) lcs

base: 
    i >= len(text1) or j >= len(text2): return 0
    
recursive:
    - if curr char are same:
        return dp (i+1 , j+1)  + 1
    - NOT same
        return max(  
            dp(i+1, j),
            dp(i, j+1),
            
        )

Time:  O(M * N) , where M is length text1 and N is length text2 (possible state combos)
Space: O(M * N)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            # recursvive decision, towards base
            # matching: can add to LIS
            if text1[i] == text2[j]:
                return dp(i+1, j+1) + 1
            else: 
                return max( dp(i+1,j), dp(i, j+1) )
        
        return dp(0,0)
    
"""
Iterative:
    - create Matrix (one dimension per state variable) to hold subproblem
    - initialize base cases
    - iterate from base cases to main problem
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        numRows = len(text1)
        numCols = len(text2)
        
        dp = [[0 for j in range(numCols + 1)] for i in range(numRows + 1)]
        
        for i in range(numRows -1, -1, -1):
            for j in range(numCols - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]