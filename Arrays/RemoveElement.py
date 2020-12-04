# https: // leetcode.com/problems/duplicate-zeros/

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
