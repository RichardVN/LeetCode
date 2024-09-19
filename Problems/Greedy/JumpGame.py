"""
Greedy solution
    - move 'goal' / good index as furthest to left as possible
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            jump_size = nums[i]
            if i + jump_size >= goal:
                goal = i
        return goal == 0

from functools import lru_cache
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        # bool
        # 'can i reach the last index, given this state i?'
        @lru_cache(None)
        def dp(i):
            # base invalid
            if i < 0 or i >= len(nums):
                return False
            # base success
            if i == len(nums) - 1:
                return True
            # recursive relation, towards right. TODO: IT NEVER MAKES SENSE GO LEFT
            jump_size = nums[i]
            for j in range(i + 1, i + jump_size + 1): #TODO: MAKE SURE ADD 1
                subRes = dp(j)
                if subRes:
                    return True
        
        return dp(0)