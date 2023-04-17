# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
"""
Why window?
- substring, continuous
- constraint: no repeats
- optimize: longest


procedure
- initialize l and r ptrs, longest substring
- for loop, expand R greedily
    - check constraint
    - while invalid, shrink with L
    - valid again. update answer
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        longest = 0
        
        chars_in_window = set()
        # try to expand window by moving right
        while right < len(s):
            # if the window is valid, no repeats for right value
            if s[right] not in chars_in_window:
                # add the character to window set
                chars_in_window.add(s[right])
                # calculate substring length, compare to current max
                longest = max(longest, right-left + 1)
                # move r for next constraint calc
                right += 1
            # window is not valid, we have to adjust beginning
            else:
                chars_in_window.remove(s[left])
                left += 1
        return longest