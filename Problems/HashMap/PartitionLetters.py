"""
https://leetcode.com/problems/partition-labels/submissions/
NOTES:
- lower case possible
- split string into AS MANY parts as possible
- for any letter, it can only appear in one partition


Approach:
Repeatedly choose the smallest left-justified position, GREEDY
We can use HASH MAP, to find the RIGHTMOST occurance of character
    - if char appears twice, it will update the value (right idx) of the key(char)
- find last occurence of letter using hash map, set right marker to that
- step through letters up until right, expanding right if rightmost is past partition
- once i == right, we append length of partition and move left

Procedure:
"""

class SolutionClean:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(s)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(s):

            right = max(right,rightmost[letter])

            if i == right:
                result += [right-left + 1]
                left = i+1

        return result
    
    
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # partition boundaries and result array
        left = 0
        right = 0
        partition_lengths = []
        
        # hash map of letter : rightmost position in string
        rightmost_idx = dict()
        for i, letter in enumerate(s):
            rightmost_idx[letter] = i
            
        for i, letter in enumerate(s):
            # for each new i, update RIGHT of partition if it is further right
            right = max(rightmost_idx[letter], right)
            
            # we have reached rightmost of partition. "create" new partition by update left, append length
            if i == right:
                # append this partition length. USE LEFT marker
                partition_lengths.append(right - left + 1)
                # update left marker to next partition
                left = i + 1
        return partition_lengths
                