"""
NOTE: KEY TAKEAWAYS:
- Constraint chars_to_flip should be <= k
    - chars_to_flip = window_lenth - most_freq_count 
- Everytime step r:  add to hash map, check if we have new most_freq_count
- Invalid state only lasts for one step until L increments
    - We NEVER have to decrement most_freq_count because it will never lead to better result

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
        char_counts = Counter()
        longest = 0
        most_freq_count = 0

        l = 0
        for r in range(len(s)):
            # update constaint
            r_char = s[r]
            char_counts[r_char] += 1  # is this most freq now?, TODO: all that matters is most_freq_COUNT
            most_freq_count = max(char_counts[r_char], most_freq_count)

            # if invalid, step with l to make valid again
            # if num_flips > k:
            if (r-l+1) - most_freq_count > k:
                # update char counter ... TODO: don't have to adjust most_freq, only way to get less num_flips is to have higher most_freq
                l_char = s[l]
                char_counts[l_char] -= 1
                # inc L
                l += 1
            # valid again
            longest = max(longest, r-l+1)

        return longest