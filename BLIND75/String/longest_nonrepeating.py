

"""
WHY sliding window?
    1.  Sequential elements data struct (LL, array, string)
    2. looking for contiguous subsection
    3. subsection has a constraint
    4. we optimize something about subsection (running max/min)


Approach: Sliding window. Set_count of all values in window
- initialize l and r ptrs
- have variable res to keep track of current best result
- LOOP r over string
    - take into account r value for constraint
    - if valid, update res
    - if not valid, move begginning of window, L until valid
"""

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        
        char_count = defaultdict(int)
        while right < len(s):
            # update window constraint
            char_count[s[right]] += 1
            
            # check if window invalid. Move left and remove from window constraint until valid
            while char_count[s[right]] > 1:
                # increment left and remove a count
                char_count[s[left]] -= 1
                left += 1
            
            # window is valid
            window_length = right - left + 1
            max_length = max(window_length, max_length)
            
            right += 1
        return max_length
            