# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

'''
NOTE: 
notice that the indices of the array
match the values of the array, if no disappearance (off by 1)

Intuition:
- Option 1: Use a set to keep track of which numbers have been seen
- Option 2: markup the original array in order to do in O(1) space
    1. Mark the indices of seen numbers as NEGATIVE.  
        NOTE: Make sure we do not access a negative index. Account for any offset (e.g. index [0, N-1] values [1, N])
        ex. "if we see value of 1, we mark the value at index 0 as negative
    2. Find a positive value, and its corresponding index/disappeared num


Space: O(1)
Time: O(n)

'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            # note we use abs. Some nums are negative ahead of ptr
            val_index = abs(num) - 1
            # mark num as seen by making its val at i - 1 negative
            # use abs in case double occurances unmark it
            nums[val_index] = abs(nums[val_index]) * -1
        # find the unmarked
        # appending to empty list, consider list comprehension
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                # ex. unmarked at i = 3, means 4 was not seen
                res.append(i+1)
        return res

        # Naive solution. Make a Hash Set of seen values.
