"""
https://leetcode.com/problems/trapping-rain-water/solution/
For each index i, the units of water trapped is:
    min(max height to left, max height to right)  -  height at i
    
        ?  
        ?       RRR
LL  //  ?   ?   RRR
    i

Two pointers L and R that start from the end
    - we know the max possible height from everything scanned left of L and right of R
        - visualize everything between L and R as "Fog"
    - At i, on the side w/ shorter wall:
        - we have seen every possible wall height to left and we KNOW there exists a right wall that will be higher
        - It doesn't matter the possible sizes of the right wall ... L has to be the limiting factor for water

Approach:
    - we can create 2 arrays that says max_height_left of i and max_height_right of i
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
                # update max_height_left AFTER calculating water
                max_height_left = max(height[left], max_height_left)
            else:
                right -= 1
                water = max(max_height_right - height[right], 0)
                result += water
                max_height_right = max(max_height_right, height[right])
                
        return result
        
        