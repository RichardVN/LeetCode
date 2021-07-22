"""
KEY: even if we make hash map  or  character count array, it is only 26 characters
            --> THIS IS CONSTANT O(1) space

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # space is O(26) which is constant
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1
        for i,c in enumerate(s):
            if char_count[ord(c) - ord('a')] == 1:
                return i
        return -1
            