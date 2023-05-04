# https://leetcode.com/problems/valid-anagram/
"""
Intuition:
- Anagram iff count of each character is equal in each string
- use Counter, to get counts of chars
- Compare the counts.. NOTE: if char is not in string, it returns 0
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        for character, count in sCounter.items():
            if count != tCounter[character]:
                return False
        return True
