"""
Approach: find if mid and target in left or right partition. Binary search

- ** 2D plot the rotated array (i, val)
- TODO: only need to handle the rotated case
- case m is in leftRotated:  when to search left or right of mid?
- case m is in rightRotated:  when to search left or right of mid?


Time : O(log n)
Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] == target:
                return m
            
            # TODO: only have to handle rotated case
            # m in left rotated .. greater or EQUAL to L
            if nums[m] >= nums[l]:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m-1
            else:
                if nums[m] > target or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
        return -1