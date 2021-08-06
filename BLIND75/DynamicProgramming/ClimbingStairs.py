"""
NOTE: FIBONACCI
DP: start from smallest problem ... 1 way to get to top from n step and n-1 step
    Original : start at 0
    smallest subproblem:  start at n
        base case: at top n step, we have 1 way to get to n step
                    second top step: 1 way to get to top
        smaller sub problem:
            - add together dp[i+1] and d[[i+2]]
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        
        for i in range(n-1):
            # store one
            temp = one
            one = one + two
            two = temp
        
        return one
        
        