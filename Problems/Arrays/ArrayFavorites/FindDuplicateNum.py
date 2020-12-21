# https://leetcode.com/problems/find-the-duplicate-number/
"""
Time: O(N) single pass through array
Space: O(1), no additional structures created. But we did write over original values

NOTE: Similar to Disappeared Nums. The big CLUE is that the range of possible values
        matches the possible indices, offset by one.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            idx_to_mark = abs(num) - 1
            # that index label has been seen
            if nums[idx_to_mark] < 0:
                return(abs(num))
            else:
                # mark that index label as seen
                nums[idx_to_mark] = - nums[idx_to_mark]
        return -1
