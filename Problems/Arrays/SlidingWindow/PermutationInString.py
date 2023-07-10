"""
create char counter dicts for Needed and Window 
variable Fulfilled: tracks how many letters we have fulfilled from needed

Sliding window Approach:
- step outward with r and add R to Window
    - increment fulfilled if Window[R] is now Needed[R]
    - reset both fulfilled and Window counter if R is NOT in Needed
    - if R overflows needed amount, while loop: increment L. TODO: update fulfilled and Window

Time: O(N) where N is size of larger string
SPACE: O(26)  .. only 26 possible chars for string

"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = Counter(s1)
        window = Counter()

        fulfilled = 0

        l = 0
        for r in range(len(s2)):
            R = s2[r]

            window[R] += 1

            # we fulfilled a needed letter count
            if window[R] == needed[R]:
                fulfilled += 1
                if fulfilled == len(needed): return True

            # if R is a "bad" letter, we have to reset 
            if R not in needed:
                fulfilled = 0
                window.clear()
                l = r + 1
                continue
            
            # TODO: if R exceeds its count, we increment L until remove another R from window
            while window[R] > needed[R]:
                L = s2[l]
                if window[L] == needed[L]:
                    fulfilled -= 1
                window[L] -= 1
                l+=1
        
        return False