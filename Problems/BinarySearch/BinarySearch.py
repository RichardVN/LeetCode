# https://leetcode.com/problems/binary-search/description/

"""
Intuition:
    - left and right markers
    - calculate new mid, eliminate half array depending if value at mid is too low or too high

TIME: O(log2N), we divide by half each time
Space: O(1, ptrs)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # TODO: less than or equal
        while l <= r:
            mid = l + (r-l)//2
            # match!
            if nums[mid] == target:
                return mid
            # too low, search higher numbers
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1 
