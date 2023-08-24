"""
What is the maxScore possible for given state

Constraint:  m operations ... one for each index i of mult

States:
    i : index of mult
    l : option for left num choice
    r : option for right num choice
Return:
    integer max Score for this subproblem

Base:
    i == len(multipliers) -> 0  ... no multipliers left
Recursive relation: 
    Right Choice:
        dp (l, r-1,  i+1)
    
    Left Choice:
        dp (l+1, r, i+1)
    return max (Left, Right)

Time: O(M^2), M combinations of (left, right) and M values for i
Space: O(M^2), Memo

"""
from functools import lru_cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # helper with state variables
        @lru_cache(None)
        def dp(left, right, i):
            # Base
            if i >= len(multipliers):
                return 0
            # recursive relations
            return max(multipliers[i] * nums[left] + dp(left + 1, right, i + 1)  ,  multipliers[i] * nums[right] + dp( left, right - 1, i + 1))

        return dp( 0, len(nums) - 1, 0)