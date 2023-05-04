"""
https://leetcode.com/problems/group-anagrams/description/
Intuition:
- anagram means: same count of chars
    -> we can use this as a key
- return: the grouped anagrams


Psuedo:
- create counts_to_word dict, with default being an empty list
- Have 26 static array character counter for each string
- convert the counter to tuple so it can be used as a key
    - append the word to the dict
- return the dict.values()
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts_to_words = defaultdict(list)

        for s in strs:
            # character count
            counts = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                print(index)
                counts[index] += 1
            # convert list to tuple so it can be immutable key
            counts = tuple(counts)
            # add counts combo : word to the dictionary
            counts_to_words[counts].append(s)
        
        # return the grouped words, aka dictionary values
        return list(counts_to_words.values())
