# https://leetcode.com/problems/duplicate-zeros/
# NOTE: Two Pointer method with read_pointer (fast) and write_pointer (slow)
# from collections import OrderedDict: useful for NO DUPLICATES, and in order
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: list[int]
        : rtype: int
        """
        last_unique = 0
        # Duplicates MUST be next to each other
        for i in range(1, len(nums)):
            if nums[i] != nums[last_unique]:  # this means nums unique
                last_unique += 1
                nums[last_unique] = nums[i]
        return last_unique + 1

        # Pythonic Answer: O(n) auxilliary space to copy into OrderedDict to remove duplicates but keep order
        # if not nums: return 0
        # nums[:] = OrderedDict.fromkeys(nums).keys()
        # return len(nums)
