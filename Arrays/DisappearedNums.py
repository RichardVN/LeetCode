# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

'''
# Space: O(1)
# Time: O(n)
# NOTE: notice that the indices of the array
# match the values of the array, if no disappearance (off by 1)
# '''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            # note we use abs. Some nums are negative, dont want -idx
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
