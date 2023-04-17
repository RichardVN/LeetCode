# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
SORTED: think of 2 pointer

SOLUTION - 2 pointer method
intuition:
    - the biggest magnitudes are at the end
    - get array from largest to smallest, then reverse
Time: O(n)
Space: O(n) for answer array
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1

        res = []
        while l <= r:
            if nums[l]**2 > nums[r]**2:
                res.append(nums[l]**2)
                l += 1
            else:
                res.append(nums[r]**2)
                r -= 1
        # array is now largest to smallest
        res.reverse()

        return res


"""
SOLUTION Alternate - use in place sort
Time: O(nlogn) due to sort
Space: O(1), overwrite in place, sort in place
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = num**2
            nums.sort()
            return nums



