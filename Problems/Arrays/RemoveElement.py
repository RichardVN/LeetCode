# https://leetcode.com/problems/remove-element/
"""
NOTE: The order can be changed --> we can use a set with O(N) space

TIP: Reword the problem. Remove all instaces of "val"  ===  Find all nums that are NOT "val"

Intuition:
    - Two pointer method
        - fast pointer reads all values of original
        - slow pointer writes in values that are not the "Bad" value
        NOTE: slow pointer never passes fast pointer

Time: O(N)
Space: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # slow pointer
        j = 0
        # fast ptr to iterate over all values
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
        return j

        # ALTERNATE: list comprehension - temporarily create O(n) auxiliary
        # nums[:] = [num for num in nums if num != val]
        # return len(nums)
