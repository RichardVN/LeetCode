"""
Sliding window clues:
    Contiguous subarray 
    Constraint of window: sum s
    Optimized variable: Minimal length window

Intuition:
    We expand the window until the elements within window have met the required sum. (1. Update j, 2. update constraint)
        If sum is met:
            We take note of the size of subarray (if it is better) and 
            shift window start until constraint is not met (1. Update constraint, 2. Update i)
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        N = len(nums)
        # value to optimize
        min_length = N + 1
        # constraint of window
        window_sum = 0

        for j in range(N):
            window_sum += nums[j]
            # while constraint is VALID, record the value. Update window until invalid
            while window_sum >= s:
                min_length = min(min_length, j-i+1)
                # update constraint from value we remove from window before increment
                window_sum -= nums[i]
                i += 1
        if min_length == N+1:
            return 0
        else:
            return min_length
