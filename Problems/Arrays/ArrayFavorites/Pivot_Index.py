"""
https://leetcode.com/problems/find-pivot-index/
NOTE: 
    - KEY: We have to do a pass to find total sum
    - at every index, we have this invariant: Sum = left_sum + val + right_sum  
    - If multiple pivots, we want left-most  -->  iterate left to right

Intuition:
    1. Do a pass to get total sum
    2. Traverse array
        a. calculate right_sum = total - left - val
        b. if left_sum == right_sum, return i
        c. add value to left_sum
    3. return -1
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # left_sum + value + right_sum = total_sum
        # check left with right. add value to left_sum at END of iteration
        total = sum(nums)
        left = 0

        for i, num in enumerate(nums):
            right = total - left - num
            if left == right:
                return i
            # update left sum before moving index
            left += num

        return -1