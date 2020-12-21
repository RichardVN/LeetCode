# https://leetcode.com/problems/duplicate-zeros/
"""
NOTE:
    - Array is SORTED. Duplicates will be next to one another
    - In place:
        - Think of shifting each element from input position to expected output position ONCE. ! Inserts would be O(N) each
        - Strategy: Look at how much each element is shifted. Is there a pattern to the shift value
    - We must shift Elements to the RIGHT. But this would make us WRITE ahead of the read pointer

Intuition:
    - First pass of array: get count of zeroes
    - Second Pass:
        - Iterate over each original value of array
        - Write the original value into its new shifted position to the right (IF it is in bounds)
        - NOTE: if we encounter a zero, we shift the original
                    THEN: we decrement count and shift the duplicate zero

Time: O(N)
Space: O(1)
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 1. get zero count
        # 2. iterate r -> l
        # 3. shift number right by zeroes before if in len array
        # 4. upon a 0: shift 0, decrease zero count, shift new 0

        zero_count = arr.count(0)
        l = len(arr)
        for i in range(l-1, -1, -1):
            if i + zero_count < l:
                # shift right all nums, even zeroes
                arr[i + zero_count] = arr[i]
            if arr[i] == 0:
                # original zero already shifted. New zero in idx one less.
                zero_count -= 1
                if i + zero_count < l:
                    arr[i+zero_count] = arr[i]
