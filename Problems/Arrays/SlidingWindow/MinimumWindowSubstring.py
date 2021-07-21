"""
Approach: Slinding window, HashMap Counts, Have and Need variables
Time :  O(S + T)  ,  O(T) to create map, O(S) to iterate with ptrs
Space:  O(S + T)   , S if window size spans S,  T if t all unique chars


- We have a Hash Count of {characters : counts} for T string
- We have a Hash Count of {characters : count} for Window Section
- We DONT want to compare both char arrays for each
    --> Instead:   Have (keeps track of char whose counts we fulfill)
    
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

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        t_counts = defaultdict(int)
        window_counts = defaultdict(int)
        
        for c in t:
            # if new key, accessing initialized to 0
            t_counts[c] += 1
        # have represents number of chars whose counts we have fulfilled
        have = 0
        # need represents number of unique chars whose counts we need to fulfill
        need = len(t_counts.keys())
        
        l, r = 0, 0
        
        res_l = res_r = -1
        res_len = float("inf")
        # expand window
        while r < len(s):
            # update constraints
            # current char
            c = s[r]
            # update window count
            window_counts[c] += 1
            # if we have met the required count for this char
            if c in t_counts and window_counts[c] == t_counts[c]:
                have += 1
                
            # if we have valid, we move l and shrink as much as possible until invalid
            while have == need:
                
                # save valid result. Need compare length, maintain l and r indices of min str
                current_len = r-l +1
                if current_len < res_len:
                    res_l = l
                    res_r = r
                    res_len = current_len
                    
                # move left pointer to shrink
                left_char = s[l]
                window_counts[left_char] -= 1
                # check if this means we no longer satisfy count for character
                if left_char in t_counts and window_counts[left_char] < t_counts[left_char]:
                    have -= 1
                # increment left
                l += 1
                
            # we are invalid, update r to try make valid
            r += 1
        return s[res_l:res_r + 1]
            