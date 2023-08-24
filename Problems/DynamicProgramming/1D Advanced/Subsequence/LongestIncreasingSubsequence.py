"""
Recursive Top down memoization

Key Points:
- we need ALL subproblems to solve question. LIS is the max of all subproblems
- subproblem[i] asks "what is Longest Incr Subsequence that ENDS with item at i?"

"""
from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            nonlocal lis
            if i == 0:
                return 1
            thisLis = 1
            for j in range(0, i):
                sub = dfs(j)    # TODO: we have to solve EVERY subproblem up to i, because total LIS can occur at any subproblem
                if nums[i] > nums[j]:
                    thisLis = max(thisLis, sub + 1)
            lis = max(lis, thisLis)
            return thisLis

        lis = 1
        dfs(len(nums) - 1)
        return lis

"""
Iterative Bottom Up
dp[i] --> ""what is LIS that ENDS with item nums[i]?""

Time: O(N^2)  , nested for loops
Space: O(N)  , dp array N items
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i], dp[j])  IF  j before i and nums[j] < nums[i]
        # dp[i] --> ""what is LIS that ENDS with item nums[i]?""
        dp = [1 for _ in nums]
        dp[0] = 1

        # solve all subproblems
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # TODO: LIS is max of any sub-LSI's
        return max(dp)