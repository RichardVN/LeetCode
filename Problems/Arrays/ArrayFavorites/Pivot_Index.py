"""
NOTE: 
    - at every index, we have this invariant: Sum = left_sum + val + right_sum  
        Given that we did a pass to get Total sum, if we know the left sum we can get the right sum in O(1)
    - If multiple pivots, we want left-most  -->  iterate left to right

Intuition:
    - we know Left sum + val + right sum  =  total_sum
    1. Do a pass to get total sum
    2. Iterate-Left-to-Right
        a. calculate right_sum
        b. if left_sum == right_sum, return i
        c. add value to left_sum
    3. return -1
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        left_sum = 0
        for i, val in enumerate(nums):
            right_sum = total_sum - left_sum - val
            if left_sum == right_sum:
                return i
            # NOTE: update left_sum AFTER comparison
            left_sum += val
        return -1
