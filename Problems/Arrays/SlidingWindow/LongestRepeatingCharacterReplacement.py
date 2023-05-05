"""
NOTE: characters are limited... ONLY 26. This is negligible work
KEY TAKEAWAYS:
- Constraint chars_to_flip should be <= k
    - chars_to_flip = window_lenth - most_freq_count 
- Everytime step r:  add to hash map, check if we have new most_freq_count

Why Window?
- Contiguous
- Constraint ... k replacements ... window length - max freq in window
- Optimize:  longest substring

Pseudo: 
- Initialize constraints, hash map for char counts
    - Step through string with r For loop
        - update map and constraint. check for new max.
        - while Invalid: chars to replace > k:
            - remove l from window. update hash map.
        - valid again. Update answer

Time: O(N),  l and r step N times, check new max is O(1)
Space: O(26)
"""
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize constraints, optimizeable
        longest = 0
        flipped = 0

        # we need to know the most common char. Use hash map
        char_counters = Counter()
        most_frequent = 0

        l = 0
        for r in range(len(s)):
            # we just stepped with r. Update constraint TODO: check max_freq AS we add to hash map
            char_counters[s[r]] += 1
            # is this now the most freq? TODO: all that matters is most_common_count, not most_common_char
            most_frequent = max(most_frequent, char_counters[s[r]])

            # shrink while invalid ... chars to flip is more than k 
            while ((r - l + 1) - most_frequent) > k:
                # remove l from window. update constraint
                char_counters[s[l]] -= 1
                l += 1

            # valid again. record answer
            longest = max(longest, r - l + 1)
        
        return longest
