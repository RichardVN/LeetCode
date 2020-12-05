# https://leetcode.com/problems/duplicate-zeros/
"""
TIPS:
    - Must be in place: think of shifting each element from original to expected ONCE, no inserts
        - Look at how much each element is shifted. What is it related to?
    - SORTED. Therefore duplicates will be next to each other
    - We shift elements RIGHT. Therefore we iterate right to left to avoid jumping ahead of iterator
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
