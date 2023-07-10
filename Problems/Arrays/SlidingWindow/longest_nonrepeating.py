# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
"""
TODO: handle invalid case first (R in Seen ... step with l pointer)
    -> THEN always add R to Seen

Why window?
- substring, continuous
- constraint: no repeats
- optimize: longest

"""
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      seen = set()
      longest = 0

      l = 0
      for r in range(len(s)):
        # invalid : saw R already.  step l until R is not in seen.
        while s[r] in seen:
          seen.remove(s[l])
          l += 1
        # update constraint, with new value at r
        longest = max(longest, r-l+1)
        seen.add(s[r]) #TODO: we always have this step even if we just handled invalid case

      return longest