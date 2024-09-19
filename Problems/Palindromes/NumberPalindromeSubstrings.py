"""
N possible centers

Time: O(N^2) ... N to go thru each center i, N to expand
Space: O(1)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            numPali = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPali += 1
                l -= 1
                r += 1
            return numPali
        
        res = 0

        for i in range(0, len(s)):
            res += expand(i, i)
            res += expand(i, i+1)

        return res