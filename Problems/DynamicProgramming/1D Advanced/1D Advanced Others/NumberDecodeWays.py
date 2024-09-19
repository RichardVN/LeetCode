"""
Time:  O(N) states
Space: O(N) states
"""
from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        @cache
        def dfs(i):
            # Base case! Empty string only has one way to decode 
            if i == len(s):
                return 1
            # starting 0 is never valid
            if s[i] == "0":
                return 0
            # can take first digit
            res = dfs(i + 1)
            # can also take 2 digits. TODO: this is only time ways branches
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            return res

        return dfs(0)