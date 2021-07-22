"""
Approach: Static char count array

Best possible solution is O(N) because we have to go over entire string to ensure non repeating
- Make character count
- Iterate over string and check if count < 4

Time: O(N) to make count array and pass thru second time
Space: O(26), 26 letters
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # "hash map" char array count , only lowercase letters
        char_count = [0] * 26
        # fill count array
        for c in s:
            char_count[ord(c) - ord('a')] += 1
        # iterate over string, return first c with count < 2
        for idx, c in enumerate(s):
            if char_count[ord(c) - ord('a')] < 2:
                return idx
        # char not found
        return -1