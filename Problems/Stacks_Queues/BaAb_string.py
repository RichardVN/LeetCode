# https: // leetcode.com/problems/make-the-string-great/discuss/780991/Clean-Python-3-stack-O(N)
"""
Add each character to 'stack'. On next character, check top of stack and pop if bad pair.
Time: O(N)
Space: O(N)
"""
class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if not result:
                result.append(c)
            elif result[-1].isupper() and result[-1].lower() == c:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == c:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
