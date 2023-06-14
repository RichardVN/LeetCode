"""
Approach: Slinding window, HashMap Counts, Have and Need variables
Time :  O(S + T)  ,  O(T) to create map, O(S) to iterate with ptrs
Space:  O(S + T)   , S if window size spans S,  T if t all unique chars

- We have a Hash Count of {characters : counts} for T string
- We have a Hash Count of {characters : count} for Window Section
TODO: For constraint, just have an int variable to keep track if we have satisfied the needed NUMBER of unique chars
    
Optimize:  minimum -> we start invalid and expand.  While valid: record, and shrink.

Procedure:
    1. Initialize hash maps. Fill t_count hash map. 
    2. Initialize Have = 0, Need = length of t_count keys
    3. Sliding window while r < len(s)
        # update constraint
        # while we are valid
            # update result if better
            # shrink window: move left pointer and update constraint
        # increment r
    4. return result with best l and r
        

"""

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = float("inf")
        min_string = ""
        l = 0

        needed_counts = Counter(t)
        window_counts = Counter()

        have = 0
        need = len(needed_counts.keys())        # unique chars we need fulfill count
        for r in range(len(s)):
            # start invalid, expand with r until valid
            # stepp with r, update counts
            letter_r = s[r]
            window_counts[letter_r] += 1

            if window_counts[letter_r] == needed_counts[letter_r]:
                have += 1

            # while valid, shrink with L
            while have == need:
                # update valid answer
                if r - l + 1 < min_window:
                    min_window = r - l + 1
                    min_string = s[l:r+1]

                letter_l = s[l]
                # we are about to remove a letter that is needed
                if window_counts[letter_l] == needed_counts[letter_l]:
                    have -= 1
                window_counts[letter_l] -= 1
                l += 1


        return min_string