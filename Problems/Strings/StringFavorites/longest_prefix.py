"""
NOTE: What is a prefix? For every string, has the same sequence of characters at front
Pythonic Solution:
- unpack strings and zip them together
- List the zip object. Now we have list of tuples containing characters
of the same index
- Check to see if all the characters in the tuple are the same, "Duplicates"
    -> Transform to set and ensure len is 1
        -> add char to prefix answer
        -> else return prefix
        
Time: O(s) where is is sum of all characters in all strings
Space: O(n) where n is num_strings, we make a temporary set for letter_group
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_chars = []
        letter_groups = list(zip(*strs))
        # [('f','f','f'), ('l','l','l'), ...]
        # step through letter groups while every letter in the group is the same
        # num_letter groups equals length of shortest string
        for letter_group in letter_groups:
            if len(set(letter_group)) == 1:
                prefix_chars.append(letter_group[0])
            else:
                break
        return ''.join(prefix_chars)


"""
More Traditional solution
NOTE: a prefix cannot be longer than the shortest word
Intuition:
- get shortest word in O(1)
- step through each char in shortest
    - for every other string, make sure it has matching char
        - if no match, return slice of shortest from 0 TO i
- made through every char in shortest
    - return shortest

Time: O(s * N) where s is chars in shortest string and N is number of strings. If all same len, this goes thru all chars of string
Space: O(1), no space created except the returned string slice of shortest
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for word in strs:
                if char != word[i]:
                    return shortest[0:i]        # up to i not including
                # else we go to next i
        # made through entire shortest, shortest IS the prefix
        return shortest
