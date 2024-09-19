"""
find longest common subsequence between s and reversed of s

STATE VAR:
- i, position in first string
- j, position in reversed string

Time: O(N^2) ... number of states
Space: O(N^2) ... number of states
"""
from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(i, j):
            # base invalid
            if i >= len(s) or j >= len(t):
                return 0

            # recursive, decisions. recursive relation.
            if s[i] == t[j]:
                return dp(i+1, j+1) + 1
            else:
                return max( dp(i+1, j), dp( i, j+1))


        t = s[::-1]

        longest = dp(i=0, j=0)
        return longest