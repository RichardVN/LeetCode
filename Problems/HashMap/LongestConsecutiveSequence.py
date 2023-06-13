"""
DRAW out the sequence blocks:
- How can we identify the begining of a consecutive sequence?  ->  Check that num - 1 does not exist
- How can we efficiently check num - 1 is not seen?  ->  Convert to hash set

Algorithm: 
- When sequence is found, keep adding to length and checking if num + length is still in the set.


TIME: O(N)  to create set, traverse each num in its correspodning sequence
NOTE: the inner while loop is ok, because we traverse each num within its sequence ONCE only.
    - worst case:  N sequences (1 num each),  or 1 huge sequence (with all N nums)

SPACE: O(N) for set
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest