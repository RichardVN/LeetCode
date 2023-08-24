"""
 [4,5,6,7,0,1,2] 

            7
            m
        6
    5
 4
 L
                            2
                            R
                        1
                    0
                    L

nums L > nums R? -> rotated
    calc mid
    if (  m in left rotated ) -> (move l to m + 1)
    else (m in right rotated ) -> (move r to m-1)
not rotated:
  return nums L

- goal is to discard half the array for each iteration
- sorted -> think binary search
- Take right half if:
    - there is still rotation

if no rotation -> can just take number at L as min

rotation?  if L > R
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # find the inflection point
        while l < r:
            m = l + (r-l)//2
            # 1. not rotated
            if nums[l] < nums[r]:
                return nums[l]

            # 2a. mid in left rotated, so min is to RIGHT
            if nums[m] > nums[l]:
                l = m+1
            # 2b. mid is in right rotated
            else:
                r = m-1

        return -1
