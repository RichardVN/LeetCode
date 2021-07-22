"""
https://leetcode.com/problems/trapping-rain-water/solution/
For each index i, the units of water trapped is:
    min(max height to left, max height to right)  -  max height at i
    
TRICK: say we are finding water level
       #
       #     Y
X      #     Y

It doesnt matter how tall the center column is, only matters that there is Y that taller

Approach:
    - we can create arrays that says max left of i and max right of i for each i
    - OR, we just have two pointers, move the one on the side with smaller height
        - height left smaller, update left
        - height right smaller, update right
        
TIME: O(2N) two pointers
SPACE: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # empty list
        if not height:
            return 0

        # initialize ptrs
        left = 0
        right = len(height) - 1
        max_height_left = height[left]
        max_height_right = height[right]
        
        result = 0
        
        while left < right:
            if max_height_left <= max_height_right:
                left += 1
                water = max(max_height_left - height[left], 0)
                result += water
                # update max_height_left
                max_height_left = max(height[left], max_height_left)
            else:
                right -= 1
                water = max(max_height_right - height[right], 0)
                result += water
                max_height_right = max(max_height_right, height[right])
                
        return result
        
        