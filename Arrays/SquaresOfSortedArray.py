# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square and overwrite in place
        for i, num in enumerate(nums):
            nums[i] = num**2
        nums.sort()
        return nums
# NOTE: this overwrites the original input array.
