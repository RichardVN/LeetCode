"""
NOTE: characters are limited... ONLY 26. This is negligible work

KEY TAKEAWAYS:
- to_replace = window_len - max_count   ... should be <= k
- we are optimizing MAX 

Why Window?
- Contiguous
- Constraint ... k replacements ... window length - max freq in window
- Optimize:  longest substring

Pseudo:
- initialize char_counter hashmap
    Expand window:
    - Update hashmap. get MaxFreq.
    - shrink while INVALID ... window_length - maxFreq > k:
        - remove from hashmap, increment l
    - Valid again. Update new best.
"""
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_counter = Counter()
        longest = 0
        mostfreq = 0

        # expand greedily, initially valid
        for r in range(len(s)):
            # we just stepped R. Update constraint (max count)
            c = s[r]
            char_counter[c] += 1
            # new max count?
            mostfreq = max(mostfreq, char_counter[c])
            
            # window length - max_count = how many letters replaced
            # while invalid ... shrink back to valid
            while (r - l + 1) - mostfreq > k:
                c = s[l]
                char_counter[c] -= 1
                l += 1

            # valid again. Update answer
            longest = max(longest, r - l + 1)

        return longest
