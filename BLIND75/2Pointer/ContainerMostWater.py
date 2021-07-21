"""
Approach: 2 Pointer, water area is width * shorter wall, move L or R inward depending which shorter
    - The water contained is always limited by min(height_l, height_r)
    - calculate water and update max
    - We move the shorter wall over, to see if we can get more water



NOTE: the bottleneck will always be the shorter of the lines

approach:
- have two pointers representing index of left line and right line of container
- have var to keep track most water
- while left < right:
    - take shorter of lines as height
    - calculate width as r - L (not inclusive)
    - update max water
    - step L or R depending on which was lower

Time: O(N)
space : O(1)

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        
        left_line = 0
        right_line = len(height) - 1
        
        most_water = 0
        
        while left_line < right_line:
            # height is minimum of the two lines
            water_height = min(height[left_line], height[right_line])
            water_width = right_line - left_line
            current_area = water_height * water_width
            
            # update most water
            most_water = max(current_area, most_water)
            
            # increment line
            if height[left_line] < height[right_line]:
                left_line += 1
            else:
                right_line -= 1
        
        return most_water