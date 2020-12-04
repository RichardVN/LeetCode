
"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        : type nums: List[int]
        : type target: int
        : returntype: List[int]
        """
        # value:index
        seen_values = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_values:
                # return the index of complement, stored in dict
                return [i, seen_values[complement]]
            else:
                seen_values[num] = i
        # no complements found
        return None
