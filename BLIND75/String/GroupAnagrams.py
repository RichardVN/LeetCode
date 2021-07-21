"""
NOTE: Tuples are immutable, and therefore HASHABLE

Approach: Get char counts of each string, tuple it, add to dictionary {char_arr: anagrams_strings_list}

Procedure
    Initialize HashMap of Char_arr : set of strings or list of strings
    1. Iterate thru every string in strs
    2. Create a character array for this string, and count chars
    3. Tuple(char_arr), add the string to hash map
    4. Step thru keys in hash map and get values

Time: Total O(N*M)  O(N) iterate thru N strings,   O(M) to count each letter in avg string
Space:  O(N*M), contains N strings of size M
"""
# import default dict to initialize to empty set when encountering new key
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        # initialize hash map for {unique_char_count : set(strings)}
        anagrams = defaultdict(list)
        
        for s in strs:
            # character array for s
            char_count = [0]*256
            
            # step thru each letter in s and add to count
            for c in s:
                idx = ord(c)
                char_count[idx] += 1
                
            # this char_count is KEY in anagrams dict. Add string to Value set
            anagrams[tuple(char_count)].append(s)
            
        # we should now have anagram dictionary {char_count1: {s1}, char_count2: {s2, s3}   }
        return list(anagrams.values())