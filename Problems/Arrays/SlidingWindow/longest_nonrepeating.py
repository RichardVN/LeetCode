# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
"""
sliding window
1.  Sequential elements data struct (LL, array, string)
2. looking for contiguous subsection
3. subsection has a constraint
4. we optimize something about subsection (running max/min)


procedure
- initialize l and r ptrs
- have variable res to keep track of current best result
- LOOP r over string
    - take into account r value for constraint
    - if valid, update res
    - if not valid, move begginning of window, L until valid
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