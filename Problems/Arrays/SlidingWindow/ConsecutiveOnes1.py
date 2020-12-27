"""
NOTE:
    - we are looking for a CONTIGUOUS subarray, that meets a certain constraint
Intuition:
    EXPAND window while meeting constraints
    SHIFT window if constraint not met, until we meet constraint again
    Sliding window where we keep track of the number of zeroes in sliding window
    Expand sliding window while we have zeroes to play with
    If we reach an overflow zero on the right, then we increment start to avoid constraint break
    NOTE: after finding a zero, we will never go to zero count of 0, because we try to expand at 1
Approach
    1. Pointers for start and end of window
    2. While loop, while end is within array bounds
        a. Increment zero count if end hits 0
        b. if zero_count overflow, move start pointer
            bi. If the start pointer was moved off 0, decrement zero_count
    3. return end - start, the biggest valid window we could expand to
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroes_in_window = 0

        start = 0
        end = 0

        while end < len(nums):
            if nums[end] == 0:
                zeroes_in_window += 1
            # we could not afford to have that zero we just added
            # move beginning of window to compensate
            # we do this until we have zeroes to spare, and we can expand w/o increasing start
            if zeroes_in_window > 1:
                start += 1
                if nums[start - 1] == 0:
                    zeroes_in_window -= 1
            end += 1
        return end - start
