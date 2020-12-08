# https://leetcode.com/problems/move-zeroes/
# NOTE: a , b = b, a variable swap is O(1)
# Optimal solution two-pointer method:
# i : slow, write pointer
# j : fast, read pointer. fast pointers can go in for loop
# anything left of slow pointer is non-zero, anything to right of slow pointer is zero or unread
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                # swap each time we encounter a non-zero we want to move to front
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
