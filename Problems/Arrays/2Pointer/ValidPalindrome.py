"""
https://leetcode.com/problems/valid-palindrome/description/

Intution:
- Walk pointers in from ends
- Skip while char if not alnum

Catches:
- make sure l and r are still valid indices before comparison
- make sure we .lower() the character before comparison
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # TODO: "skip" ptr if char is not alnum. 
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            # TODO: Check pointers are still valid
            # TODO: convert alnum to lower
            if s[l].lower() != s[r].lower() and l < r:
                return False
            
            l += 1
            r -= 1
        return True