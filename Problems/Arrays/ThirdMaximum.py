# https://leetcode.com/problems/third-maximum-number/
"""
NOTE: 
    - Usually to keep track of max we can just have a max variable
    - If we need the THIRD max, we can just have three variables for the top 3 numbers
        - For each num: do a check and see if it slots into top 3. Shift the other max right accordingly
        
Only need three variables. This is CONSTANT space
TIME: O(n) to loop and compare to max
SPACE: O(3) ~ O(1)
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_1, max_2, max_3 = -float("inf"), -float("inf"), -float("inf")

        # see where num fits among maximums, and shift accordingly
        # if num is exactly equal to max, dont do anything
        for num in nums:
            if num > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif max_1 > num and num > max_2:
                max_3 = max_2
                max_2 = num
            elif max_2 > num and num > max_3:
                max_3 = num
        return max_3 if max_3 > -float("inf") else max_1
