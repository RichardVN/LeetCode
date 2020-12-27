# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
NOTE:
    - sorted array => duplicates must be next to one another
    - reword problem: find Unique nums

Intuition:
    - Fast pointer: read original values
    - Slow pointer: write unique nums

Alternative: hashset to remove duplicates

Time: O(N)
Space: O(1)
"""
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
