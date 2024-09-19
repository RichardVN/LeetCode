"""
subsets can only be equal of total sum of nums is even

Trying to find subset / combination of nums such that it equals sum(nums) // 2
TODO: - Combinations -> Take or Skip choice. **If we take, we canot re-use...go to i + 1 state

dp Helper
- "For given state: target and i, is it possible to reach target sum?"
- Base invalid: target < 0 or i out of bounds -> False
- Base smallest: target == 0 -> True
- Recursive relation:
    - Return True iff Take -> True OR Skip -> True

Time / Space: O(N * target//2)
"""
from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, target):
            if target < 0 or i >= len(nums):
                return False
            if target == 0:
                return True
            
            take = dp(i+1, target - nums[i])
            skip = dp(i+1, target)
            return take or skip
        
        if sum(nums) %2 != 0:
            return False
        
        target = sum(nums) // 2

        return dp(0, target)
        
