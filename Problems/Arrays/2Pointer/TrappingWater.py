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
        
TIME: O(N) two pointers walk in
SPACE: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        tallest_l = height[l]
        tallest_r = height[r]

        water = 0

        while l < r:
            # l is guaranteed shorter wall
            if tallest_l < tallest_r:
                l += 1
                # 0 or greater. add water at this index
                water += max(tallest_l - height[l], 0)
                # update max seen on left
                tallest_l = max(tallest_l, height[l])
            else:
                r -= 1
                water += max(tallest_r - height[r], 0)
                tallest_r = max(tallest_r, height[r])

        return water

        