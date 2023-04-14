# https://leetcode.com/problems/duplicate-zeros/
"""
Naive solution: iterate right to left and use .insert()

NOTE:
    - In place:
        - Think of shifting each element from input position to expected output position ONCE. ! Inserts would be O(N) each
        - Strategy: Look at how much each element is shifted. Is there a pattern to the shift value
    - We must shift Elements to the RIGHT. But this would make us WRITE ahead of the read pointer

Intuition:
    - Compare initial input with expected, see the pattern of how much each element is shifted
    - 1. get count of zeroes using .count()
    - 2.  Traverse array Right to Left
        1. Write the original value (INCLUDING zeroes) into its new shifted position to the right (IF it is in bounds)
        2. NOTE: IF we are on a zero, we decrement count and shift the duplicate zero

Time: O(N)
Space: O(1)
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 1. get zero count
        # 2. iterate r -> l so we dont overwrite changed values
        # 3. shift value at current index to right by amount of zeroes to left, if shifted location is within len array
        # 4. upon a 0: shift 0, decrease zero count, shift new 0

        zero_count = arr.count(0)
        l = len(arr)

        for i in range(l-1, -1, -1):
            # shift right all nums, even original zeroes
            if i + zero_count < l:
                arr[i + zero_count] = arr[i]
                
            # original zero already shifted in if block above. Now duplicate zero in index before original.
            if arr[i] == 0:
                zero_count -= 1
                if i + zero_count < l:
                    arr[i + zero_count] = arr[i]
