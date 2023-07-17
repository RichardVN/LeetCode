# https://leetcode.com/problems/max-consecutive-ones/description/

"""
Intuition: using running variable
    - Traverse and increment streak count if 1
    - if not 1, reset streak to 0

NOTE : no need for sliding window:  we never increment L incrementally to update constraint
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxStreak = 0
        runningStreak  = 0

        for num in nums:
            runningStreak = runningStreak + 1 if num == 1 else 0
            maxStreak = max(maxStreak, runningStreak)
        return maxStreak
